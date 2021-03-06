
package com.tinkerforge;

import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.time.ZonedDateTime;
import java.util.concurrent.CopyOnWriteArrayList;
import java.util.Arrays;
import java.util.List;
import java.net.URI;
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Collections;
import java.util.function.Function;

import com.tinkerforge.BrickletOutdoorWeather.StationData;
import com.tinkerforge.Device.SetterRefresh;

import java.util.function.BiConsumer;
import org.eclipse.smarthome.config.core.Configuration;
import org.eclipse.smarthome.config.core.ConfigDescription;
import org.eclipse.smarthome.config.core.ConfigDescriptionParameter.Type;
import org.eclipse.smarthome.config.core.ConfigDescriptionParameterBuilder;
import org.eclipse.smarthome.config.core.ConfigDescriptionParameterGroup;
import org.eclipse.smarthome.config.core.ParameterOption;
import org.eclipse.smarthome.core.types.State;
import org.eclipse.smarthome.core.types.StateOption;
import org.eclipse.smarthome.core.types.Command;
import org.eclipse.smarthome.core.types.CommandDescriptionBuilder;
import org.eclipse.smarthome.core.types.CommandOption;
import org.eclipse.smarthome.core.thing.ThingTypeUID;
import org.eclipse.smarthome.core.thing.type.ChannelDefinitionBuilder;
import org.eclipse.smarthome.core.thing.type.ChannelType;
import org.eclipse.smarthome.core.thing.type.ChannelTypeBuilder;
import org.eclipse.smarthome.core.thing.type.ChannelTypeUID;
import org.eclipse.smarthome.core.thing.type.ThingType;
import org.eclipse.smarthome.core.thing.type.ThingTypeBuilder;
import org.eclipse.smarthome.core.types.StateDescriptionFragmentBuilder;
import org.eclipse.smarthome.binding.tinkerforge.internal.TinkerforgeBindingConstants;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.eclipse.smarthome.core.library.types.DateTimeType;
import org.eclipse.smarthome.core.library.types.OnOffType;
import org.eclipse.smarthome.core.library.types.QuantityType;
import org.eclipse.smarthome.core.library.types.StringType;
import org.eclipse.smarthome.core.library.unit.MetricPrefix;
import org.eclipse.smarthome.core.library.unit.SIUnits;
import org.eclipse.smarthome.core.library.unit.SmartHomeUnits;


public class BrickletOutdoorWeatherStation {
    public BrickletOutdoorWeatherStation(int id, BrickletOutdoorWeather bricklet) {
        this.id = id;
        this.bricklet = bricklet;
    }

    private final int id;
    private final BrickletOutdoorWeather bricklet;

    public final static int DEVICE_IDENTIFIER = -288;
    public final static String DEVICE_DISPLAY_NAME = "Outdoor Weather Station";

    public final static DeviceInfo DEVICE_INFO = new DeviceInfo(DEVICE_DISPLAY_NAME, "outdoorweatherstation",
            DEVICE_IDENTIFIER, BrickletOutdoorWeatherStation.class);

    private final Logger logger = LoggerFactory.getLogger(BrickletOutdoorWeather.class);
    private final static Logger static_logger = LoggerFactory.getLogger(BrickletOutdoorWeather.class);

    public void initialize(org.eclipse.smarthome.config.core.Configuration config, Function<String, org.eclipse.smarthome.config.core.Configuration> getChannelConfigFn, BiConsumer<String, org.eclipse.smarthome.core.types.State> updateStateFn, BiConsumer<String, String> triggerChannelFn) {
        bricklet.addStationDataListener((int identifier, int temperature, int humidity, long windSpeed, long gustSpeed, long rain, int windDirection, boolean batteryLow) -> {
            if(identifier != this.id)
                return;
            updateStateFn.accept("OutdoorWeatherStationTemperature",   new QuantityType<>(temperature / 10.0, SIUnits.CELSIUS));
            updateStateFn.accept("OutdoorWeatherStationHumidity",      new QuantityType<>(humidity, SmartHomeUnits.PERCENT));
            updateStateFn.accept("OutdoorWeatherStationWindSpeed",     new QuantityType<>(windSpeed / 10.0, SmartHomeUnits.METRE_PER_SECOND));
            updateStateFn.accept("OutdoorWeatherStationGustSpeed",     new QuantityType<>(gustSpeed / 10.0, SmartHomeUnits.METRE_PER_SECOND));
            updateStateFn.accept("OutdoorWeatherStationRainFall",      new QuantityType<>(rain / 10000.0, SIUnits.METRE));
            updateStateFn.accept("OutdoorWeatherStationWindDirection", new StringType(getWindDirectionName(windDirection)));
            updateStateFn.accept("OutdoorWeatherStationBatteryLow",    batteryLow ? OnOffType.ON : OnOffType.OFF);
            updateStateFn.accept("OutdoorWeatherStationLastChange",    new DateTimeType(getAbsoluteTime(0)));
        });
    }

    public List<String> getEnabledChannels(org.eclipse.smarthome.config.core.Configuration config)
            throws TinkerforgeException {
        return Arrays.asList("OutdoorWeatherStationTemperature",
                             "OutdoorWeatherStationHumidity",
                             "OutdoorWeatherStationWindSpeed",
                             "OutdoorWeatherStationGustSpeed",
                             "OutdoorWeatherStationRainFall",
                             "OutdoorWeatherStationWindDirection",
                             "OutdoorWeatherStationBatteryLow",
                             "OutdoorWeatherStationLastChange");
    }

    public static ChannelType getChannelType(ChannelTypeUID channelTypeUID) {
        switch (channelTypeUID.getId()) {
        case "OutdoorWeatherStationTemperature":
            return ChannelTypeBuilder
                    .state(new ChannelTypeUID("tinkerforge", "OutdoorWeatherStationTemperature"), "Temperature",
                            "Number:Temperature")
                    .withConfigDescriptionURI(URI.create("channel-type:tinkerforge:OutdoorWeatherStationTemperature"))
                    .withDescription("Last received temperature").withStateDescription(StateDescriptionFragmentBuilder
                            .create().withPattern("%.1f %unit%").withReadOnly(true).build().toStateDescription())
                    .build();
        case "OutdoorWeatherStationHumidity":
            return ChannelTypeBuilder
                    .state(new ChannelTypeUID("tinkerforge", "OutdoorWeatherStationHumidity"), "Humidity",
                            "Number:Dimensionless")
                    .withConfigDescriptionURI(URI.create("channel-type:tinkerforge:OutdoorWeatherStationHumidity"))
                    .withDescription("Last received humidity").withStateDescription(StateDescriptionFragmentBuilder
                            .create().withPattern("%d %%").withReadOnly(true).build().toStateDescription())
                    .build();
        case "OutdoorWeatherStationWindSpeed":
            return ChannelTypeBuilder
                    .state(new ChannelTypeUID("tinkerforge", "OutdoorWeatherStationWindSpeed"), "Wind Speed", "Number:Speed")
                    .withConfigDescriptionURI(URI.create("channel-type:tinkerforge:OutdoorWeatherStationWindSpeed"))
                    .withDescription("Last received wind speed").withStateDescription(StateDescriptionFragmentBuilder
                            .create().withPattern("%.1f %unit%").withReadOnly(true).build().toStateDescription())
                    .build();
        case "OutdoorWeatherStationGustSpeed":
            return ChannelTypeBuilder
                    .state(new ChannelTypeUID("tinkerforge", "OutdoorWeatherStationGustSpeed"), "Gust Speed", "Number:Speed")
                    .withConfigDescriptionURI(URI.create("channel-type:tinkerforge:OutdoorWeatherStationGustSpeed"))
                    .withDescription("Last received gust speed").withStateDescription(StateDescriptionFragmentBuilder
                            .create().withPattern("%.1f %unit%").withReadOnly(true).build().toStateDescription())
                    .build();
        case "OutdoorWeatherStationRainFall":
            return ChannelTypeBuilder
                    .state(new ChannelTypeUID("tinkerforge", "OutdoorWeatherStationRainFall"), "Rain Fall", "Number:Length")
                    .withConfigDescriptionURI(URI.create("channel-type:tinkerforge:OutdoorWeatherStationRainFall"))
                    .withDescription("Last received rain fall.").withStateDescription(StateDescriptionFragmentBuilder
                            .create().withPattern("%.4f %unit%").withReadOnly(true).build().toStateDescription())
                    .build();
        case "OutdoorWeatherStationWindDirection":
            return ChannelTypeBuilder
                    .state(new ChannelTypeUID("tinkerforge", "OutdoorWeatherStationWindDirection"), "Wind Direction", "String")
                    .withConfigDescriptionURI(URI.create("channel-type:tinkerforge:OutdoorWeatherStationWindDirection"))
                    .withDescription("Last received wind direction")
                    .withStateDescription(
                            StateDescriptionFragmentBuilder.create().withReadOnly(true).build().toStateDescription())
                    .build();
        case "OutdoorWeatherStationBatteryLow":
            return ChannelTypeBuilder
                    .state(new ChannelTypeUID("tinkerforge", "OutdoorWeatherStationBatteryLow"), "Battery Low", "Switch")
                    .withConfigDescriptionURI(URI.create("channel-type:tinkerforge:OutdoorWeatherStationBatteryLow"))
                    .withDescription("Enabled if battery is low.")
                    .withStateDescription(
                            StateDescriptionFragmentBuilder.create().withReadOnly(true).build().toStateDescription())
                    .build();
        case "OutdoorWeatherStationLastChange":
            return ChannelTypeBuilder
                    .state(new ChannelTypeUID("tinkerforge", "OutdoorWeatherStationLastChange"), "Last Change", "DateTime")
                    .withConfigDescriptionURI(URI.create("channel-type:tinkerforge:OutdoorWeatherStationLastChange"))
                    .withDescription("Time when the last data was received from the station. The station sends data every 45 to 60 seconds.")
                    .withStateDescription(
                            StateDescriptionFragmentBuilder.create().withReadOnly(true).build().toStateDescription())
                    .build();
        default:
            static_logger.debug("Unknown channel type ID {}", channelTypeUID.getId());
            break;
        }

        return null;
    }

    public static ThingType getThingType(ThingTypeUID thingTypeUID) {
        return ThingTypeBuilder.instance(thingTypeUID, "Tinkerforge Outdoor Weather Station WS-6147.").isListed(false)
                .withSupportedBridgeTypeUIDs(Arrays.asList(TinkerforgeBindingConstants.THING_TYPE_OUTDOOR_WEATHER.getId()))
                .withConfigDescriptionURI(URI.create("thing-type:tinkerforge:" + thingTypeUID.getId()))
                .withDescription("Weather Station connected to an Outdoor Weather Bricklet")
                .withChannelDefinitions(Arrays.asList(
                        new ChannelDefinitionBuilder("OutdoorWeatherStationTemperature",
                                new ChannelTypeUID("tinkerforge", "OutdoorWeatherStationTemperature")).withLabel("Temperature").build(),
                        new ChannelDefinitionBuilder("OutdoorWeatherStationHumidity",
                                new ChannelTypeUID("tinkerforge", "OutdoorWeatherStationHumidity")).withLabel("Humidity").build(),
                        new ChannelDefinitionBuilder("OutdoorWeatherStationWindSpeed",
                                new ChannelTypeUID("tinkerforge", "OutdoorWeatherStationWindSpeed")).withLabel("Wind Speed").build(),
                        new ChannelDefinitionBuilder("OutdoorWeatherStationGustSpeed",
                                new ChannelTypeUID("tinkerforge", "OutdoorWeatherStationGustSpeed")).withLabel("Gust Speed").build(),
                        new ChannelDefinitionBuilder("OutdoorWeatherStationRainFall",
                                new ChannelTypeUID("tinkerforge", "OutdoorWeatherStationRainFall")).withLabel("Rain Fall").build(),
                        new ChannelDefinitionBuilder("OutdoorWeatherStationWindDirection",
                                new ChannelTypeUID("tinkerforge", "OutdoorWeatherStationWindDirection")).withLabel("Wind Direction").build(),
                        new ChannelDefinitionBuilder("OutdoorWeatherStationBatteryLow",
                                new ChannelTypeUID("tinkerforge", "OutdoorWeatherStationBatteryLow")).withLabel("Battery Low").build(),
                        new ChannelDefinitionBuilder("OutdoorWeatherStationLastChange",
                                new ChannelTypeUID("tinkerforge", "OutdoorWeatherStationLastChange")).withLabel("Last Change").build()))
                .build();
    }

    public static ConfigDescription getConfigDescription(URI uri) {
        switch (uri.toASCIIString()) {
        case "thing-type:tinkerforge:outdoorweatherstation":
        case "channel-type:tinkerforge:OutdoorWeatherStationTemperature":
        case "channel-type:tinkerforge:OutdoorWeatherStationHumidity":
        case "channel-type:tinkerforge:OutdoorWeatherStationWindSpeed":
        case "channel-type:tinkerforge:OutdoorWeatherStationGustSpeed":
        case "channel-type:tinkerforge:OutdoorWeatherStationRainFall":
        case "channel-type:tinkerforge:OutdoorWeatherStationWindDirection":
        case "channel-type:tinkerforge:OutdoorWeatherStationBatteryLow":
        case "channel-type:tinkerforge:OutdoorWeatherStationLastChange":
            return new ConfigDescription(uri, Arrays.asList());
        default:
            static_logger.debug("Unknown config description URI {}", uri.toASCIIString());
            break;
        }
        return null;
    }


    public void refreshValue(String value, org.eclipse.smarthome.config.core.Configuration config, org.eclipse.smarthome.config.core.Configuration channelConfig, BiConsumer<String, org.eclipse.smarthome.core.types.State> updateStateFn, BiConsumer<String, String> triggerChannelFn) throws TinkerforgeException {
        switch(value) {
            case "OutdoorWeatherStationTemperature":
                updateStateFn.accept(value, transformOutdoorWeatherTemperatureGetter0(bricklet.getStationData(this.id)));
                break;
            case "OutdoorWeatherStationHumidity":
                updateStateFn.accept(value, transformOutdoorWeatherHumidityGetter0(bricklet.getStationData(this.id)));
                break;
            case "OutdoorWeatherStationWindSpeed":
                updateStateFn.accept(value, transformOutdoorWeatherWindSpeedGetter0(bricklet.getStationData(this.id)));
                break;
            case "OutdoorWeatherStationGustSpeed":
                updateStateFn.accept(value, transformOutdoorWeatherGustSpeedGetter0(bricklet.getStationData(this.id)));
                break;
            case "OutdoorWeatherStationRainFall":
                updateStateFn.accept(value, transformOutdoorWeatherRainFallGetter0(bricklet.getStationData(this.id)));
                break;
            case "OutdoorWeatherStationWindDirection":
                updateStateFn.accept(value, transformOutdoorWeatherWindDirectionGetter0(bricklet.getStationData(this.id)));
                break;
            case "OutdoorWeatherStationBatteryLow":
                updateStateFn.accept(value, transformOutdoorWeatherBatteryLowGetter0(bricklet.getStationData(this.id)));
                break;
            case "OutdoorWeatherStationLastChange":
                updateStateFn.accept(value, transformOutdoorWeatherLastChangeGetter0(bricklet.getStationData(this.id)));
                break;
            default:
                logger.warn("Refresh for unknown channel {}", value);
                break;
        }
    }

    public String getWindDirectionName(int windDirection) {
        String[] windDirections = new String[] {
            "N",
            "NNE",
            "NE",
            "ENE",
            "E",
            "ESE",
            "SE",
            "SSE",
            "S",
            "SSW",
            "SW",
            "WSW",
            "W",
            "WNW",
            "NW",
            "NNW"
        };

        if(windDirection >= 0 && windDirection < windDirections.length) {
            return windDirections[windDirection];
        } else if (windDirection == 255) {
            return "Unknown (Station Error)";
        } else {
            return "Unknown (" + windDirection + ")";
        }
    }

    public ZonedDateTime getAbsoluteTime(int offset) {
        return ZonedDateTime.now().minusSeconds(offset);
    }

    public List<SetterRefresh> handleCommand(org.eclipse.smarthome.config.core.Configuration config, org.eclipse.smarthome.config.core.Configuration channelConfig, String channel, Command command) throws TinkerforgeException {
        List<SetterRefresh> result = Collections.emptyList();
        switch(channel) {

            default:
                logger.warn("Command for unknown channel {}", channel);
        }
        return result;
    }


    private org.eclipse.smarthome.core.types.State transformOutdoorWeatherTemperatureGetter0(StationData value) {
        return new QuantityType<>(value.temperature / 10.0, SIUnits.CELSIUS);
    }
    private org.eclipse.smarthome.core.types.State transformOutdoorWeatherHumidityGetter0(StationData value) {
        return new QuantityType<>(value.humidity, SmartHomeUnits.PERCENT);
    }
    private org.eclipse.smarthome.core.types.State transformOutdoorWeatherWindSpeedGetter0(StationData value) {
        return new QuantityType<>(value.windSpeed / 10.0, SmartHomeUnits.METRE_PER_SECOND);
    }
    private org.eclipse.smarthome.core.types.State transformOutdoorWeatherGustSpeedGetter0(StationData value) {
        return new QuantityType<>(value.gustSpeed / 10.0, SmartHomeUnits.METRE_PER_SECOND);
    }
    private org.eclipse.smarthome.core.types.State transformOutdoorWeatherRainFallGetter0(StationData value) {
        return new QuantityType<>(value.rain / 10000.0, SIUnits.METRE);
    }
    private org.eclipse.smarthome.core.types.State transformOutdoorWeatherWindDirectionGetter0(StationData value) {
        return new StringType(getWindDirectionName(value.windDirection));
    }
    private org.eclipse.smarthome.core.types.State transformOutdoorWeatherBatteryLowGetter0(StationData value) {
        return value.batteryLow ? OnOffType.ON : OnOffType.OFF;
    }
    private org.eclipse.smarthome.core.types.State transformOutdoorWeatherLastChangeGetter0(StationData value) {
        return new DateTimeType(getAbsoluteTime(value.lastChange));
    }
}
