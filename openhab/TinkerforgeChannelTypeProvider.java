package org.eclipse.smarthome.binding.tinkerforge.internal;

import java.lang.reflect.InvocationTargetException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.HashMap;
import java.util.Locale;
import java.util.Map;
import java.util.stream.Collectors;

import com.tinkerforge.DeviceFactory;
import com.tinkerforge.DeviceInfo;

import org.eclipse.jdt.annotation.Nullable;
import org.eclipse.smarthome.core.thing.ThingTypeUID;
import org.eclipse.smarthome.core.thing.type.ChannelDefinition;
import org.eclipse.smarthome.core.thing.type.ChannelDefinitionBuilder;
import org.eclipse.smarthome.core.thing.type.ChannelType;
import org.eclipse.smarthome.core.thing.type.ChannelTypeProvider;
import org.eclipse.smarthome.core.thing.type.ChannelTypeUID;
import org.eclipse.smarthome.core.thing.type.ThingTypeBuilder;
import org.osgi.service.component.ComponentContext;
import org.osgi.service.component.annotations.Activate;
import org.osgi.service.component.annotations.Component;
import org.osgi.service.component.annotations.Deactivate;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@Component(service = ChannelTypeProvider.class, immediate = true)
public class TinkerforgeChannelTypeProvider implements ChannelTypeProvider {

    private static final Map<ChannelTypeUID, ChannelType> channelTypeCache = new HashMap<>();

    private final static Logger logger = LoggerFactory.getLogger(TinkerforgeChannelTypeProvider.class);

    @Activate
    protected void activate(ComponentContext componentContext) {
        logger.trace("Activate");
    }

    @Deactivate
    protected void deactivate(ComponentContext componentContext) {
        logger.trace("Deactivate");
    }

    @Override
    public Collection<ChannelType> getChannelTypes(@Nullable Locale locale) {
        return TinkerforgeBindingConstants.SUPPORTED_CHANNELS.keySet().stream().map(uid -> getChannelType(uid, locale))
                .collect(Collectors.toList());
    }

    @Override
    public @Nullable ChannelType getChannelType(ChannelTypeUID channelTypeUID, @Nullable Locale locale) {
        return getChannelTypeStatic(channelTypeUID, locale);
    }

    public static @Nullable ChannelType getChannelTypeStatic(ChannelTypeUID channelTypeUID, @Nullable Locale locale) {
        if (channelTypeCache.containsKey(channelTypeUID)) {
            return channelTypeCache.get(channelTypeUID);
        }

        ThingTypeUID thingTypeUID = null;
        DeviceInfo info = null;
        try {
            thingTypeUID = TinkerforgeBindingConstants.SUPPORTED_CHANNELS.get(channelTypeUID);
            info = DeviceFactory.getDeviceInfo(thingTypeUID.getId());
        }
        catch (Exception e) {
            logger.debug("Could not find device info for channelTypeUID {}: {}.", channelTypeUID, e.getMessage());
            return null;
        }
        ChannelType result = null;
        try {
            result = (ChannelType) info.deviceClass.getMethod("getChannelType", ChannelTypeUID.class).invoke(null,
                    channelTypeUID);
        } catch (Exception e) {
            logger.debug("Could not find channel type for channelTypeUID {} of device {}: {}.", channelTypeUID, info.deviceDisplayName, e.getMessage());
            return null;
        }


        channelTypeCache.put(channelTypeUID, result);
        return result;
    }
}
