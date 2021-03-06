package org.eclipse.smarthome.binding.tinkerforge.internal;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.stream.Collectors;

import com.tinkerforge.BrickDaemon;
import com.tinkerforge.DeviceFactory;
import com.tinkerforge.DeviceInfo;

import org.eclipse.jdt.annotation.Nullable;
import org.eclipse.smarthome.core.thing.ThingTypeUID;
import org.eclipse.smarthome.core.thing.binding.ThingTypeProvider;
import org.eclipse.smarthome.core.thing.type.ThingType;
import org.eclipse.smarthome.core.thing.type.ThingTypeBuilder;
import org.osgi.service.component.annotations.Component;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@Component(service = ThingTypeProvider.class, immediate = true)
public class TinkerforgeThingTypeProvider implements ThingTypeProvider {

    private static final Map<ThingTypeUID, ThingType> thingTypeCache = new HashMap<>();
    private final static Logger logger = LoggerFactory.getLogger(TinkerforgeChannelTypeProvider.class);

    @Override
    public Collection<ThingType> getThingTypes(@Nullable Locale locale) {
        return TinkerforgeBindingConstants.SUPPORTED_DEVICES.stream().map(uid -> getThingType(uid, locale))
                .collect(Collectors.toList());
    }

    @Override
    public @Nullable ThingType getThingType(ThingTypeUID thingTypeUID, @Nullable Locale locale) {
        return getThingTypeStatic(thingTypeUID, locale);
    }

    public static @Nullable ThingType getThingTypeStatic(ThingTypeUID thingTypeUID, @Nullable Locale locale) {
        if (thingTypeCache.containsKey(thingTypeUID)) {
            return thingTypeCache.get(thingTypeUID);
        }

        DeviceInfo info = null;
        try {
            info = DeviceFactory.getDeviceInfo(thingTypeUID.getId());
        }
        catch (Exception e) {
            logger.debug("Could not find device info for thingTypeUID {}: {}.", thingTypeUID, e.getMessage());
            return null;
        }
        ThingType result;
        try {
            Method m = info.deviceClass.getMethod("getThingType", ThingTypeUID.class);
            result = (ThingType) m.invoke(null, thingTypeUID);
        } catch (Exception e) {
            logger.debug("Could not find thing type for thingTypeUID {} of device {}: {}.", thingTypeUID, info.deviceDisplayName, e.getMessage());
            return null;
        }

        thingTypeCache.put(thingTypeUID, result);
        return result;
    }
}
