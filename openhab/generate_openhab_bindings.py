#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
MATLAB/Octave Bindings Generator
Copyright (C) 2019 Erik Fleckstein <erik@tinkerforge.com>

generate_openhab_bindings.py: Generator for OpenHAB bindings

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public
License along with this program; if not, write to the
Free Software Foundation, Inc., 59 Temple Place - Suite 330,
Boston, MA 02111-1307, USA.
"""

from collections import namedtuple
import os
import sys

sys.path.append(os.path.split(os.getcwd())[0])
sys.path.append(os.path.join(os.path.split(os.getcwd())[0], 'java'))
import common
from java.generate_java_bindings import JavaBindingsGenerator, JavaBindingsDevice


# TODO: Maybe read this directly from schema documentation
OPENHAB_PARAM_ATTRS = [
    "name",
    "type",
    "groupName",
    "min",
    "max",
    "step",
    "pattern",
    "required",
    "readOnly",
    "multiple",
    "unit"
]

OPENHAB_PARAM_ELEMENTS = [
    "context",
    "required",
    "default",
    "label",
    "description",
    # options and filter are handled separately.
    #"options",
    "limitToOptions",
    #"filter",
    "advanced",
    "verify",
    "multipleLimit",
    "unitLabel"
]

OPENHAB_PARAM_GROUP_ELEMENTS = [
    "label",
    "description",
    "context",
    "advanced"
]

class OpenHABBindingsDevice(JavaBindingsDevice):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not 'openhab' in self.raw_data:
            return

        oh = self.raw_data['openhab']

        channel_defaults = {
            'params': [],
            'init_code': '',
            'dispose_code': '',
            'getter_packet_params': [],
            'setter_packet': None,
            'setter_packet_params': [],
            'setter_command_type': None,
            'callback_packet': None,

            'callback_param_mapping': None,
            'callback_filter': 'true',
            'java_unit': None,
            'divisor': 1,
            'is_trigger_channel': False,
            'predicate': 'true',

            'label': None,
            'description': None
        }

        oh_defaults = {
            'params': [],
            'param_groups': [],
            'init_code': '',
            'dispose_code': '',
        }

        tmp = oh_defaults.copy()
        tmp.update(oh)
        oh = tmp

        for c_idx, channel in enumerate(oh['channels']):
            tmp = channel_defaults.copy()
            tmp.update(channel)
            oh['channels'][c_idx] = tmp

        # Replace config placeholders
        def fmt(format_str, base_name, unit, divisor):
            if not isinstance(format_str, str):
                return format_str
            name = common.FlavoredName(base_name).get()
            return format_str.format(title_words=name.space.title(),
                                     lower_words=name.lower,
                                     camel=name.camel,
                                     headless=name.headless,
                                     unit=unit,
                                     divisor=' / ' + str(divisor) if divisor != 1 else '')

        for c_idx, channel in enumerate(oh['channels']):
            for p_idx, param in enumerate(channel['params']):
                channel['params'][p_idx] = {k: fmt(v, channel['id'], param['unit'], 1) for k, v in channel['params'][p_idx].items()}
            oh['channels'][c_idx] = {k: fmt(v, channel['id'], channel['java_unit'], channel['divisor']) for k, v in oh['channels'][c_idx].items()}

        # Convert from dicts to namedtuples
        OpenHAB = namedtuple('OpenHAB', ['channels', 'channel_types', 'imports', 'params', 'param_groups', 'init_code', 'dispose_code'])
        Channel = namedtuple('Channel', ['id', 'type_id', 'params', 'init_code', 'dispose_code',
                                         'java_unit', 'divisor', 'is_trigger_channel', 'transform',
                                         'getter_packet', 'getter_packet_params',
                                         'setter_packet', 'setter_packet_params', 'setter_command_type',
                                         'callback_packet', 'callback_param_mapping', 'callback_filter',
                                         'predicate',
                                         'label', 'description'])
        Param = namedtuple('Param', ['name', 'type', 'default', 'attrs', 'elements', 'options', 'filter'])
        ParamGroup = namedtuple('ParamGroup', ['name', 'elements'])
        ChannelType = namedtuple('ChannelType', 'type_id item_type label description read_only pattern min max')

        def param_dict_to_tup(param):
            name = common.FlavoredName(param['name']).get()
            attrs = {k: v for k, v in param.items() if k in OPENHAB_PARAM_ATTRS}
            attrs['name'] = name.headless
            return Param(name=name,
                        type=param['type'],
                        default=param['default'],
                        attrs=attrs,
                        elements={k: v for k, v in param.items() if k in OPENHAB_PARAM_ELEMENTS},
                        options={right: left for left, right in param['options']} if 'options' in param else dict(),
                        filter={right: left for left, right in param['filter']} if 'filter' in param else dict())

        def find_packet(name):
            if name is None:
                return None
            return next(p for p in self.get_packets() if p.get_name().space == name)

        for c_idx, channel in enumerate(oh['channels']):
            for p_idx, param in enumerate(channel['params']):
                channel['params'][p_idx] = param_dict_to_tup(param)
            for packet in ['getter_packet', 'setter_packet', 'callback_packet']:
                oh['channels'][c_idx][packet] = find_packet(oh['channels'][c_idx][packet])
            if oh['channels'][c_idx]['callback_param_mapping'] is not None:
                oh['channels'][c_idx]['callback_param_mapping'] = {common.FlavoredName(k).get(): (common.FlavoredName(v).get() if v is not None else None) for k, v in oh['channels'][c_idx]['callback_param_mapping'].items()}
            oh['channels'][c_idx] = Channel(**channel)

        for ct_idx, channel_type in enumerate(oh['channel_types']):
            oh['channel_types'][ct_idx] = ChannelType(**channel_type)

        for p_idx, param in enumerate(oh['params']):
            oh['params'][p_idx] = param_dict_to_tup(param)

        for g_idx, group in enumerate(oh['param_groups']):
            oh['param_groups'][g_idx] = ParamGroup(name=group['name'],
                                                   elements={k: v for k, v in group.items() if k in OPENHAB_PARAM_GROUP_ELEMENTS})

        self.oh = OpenHAB(**oh)

    def get_java_import(self):
        java_imports = super().get_java_import()
        oh_imports = ['java.util.ArrayList', 'java.util.function.BiConsumer', 'org.eclipse.smarthome.core.types.State', 'org.eclipse.smarthome.core.types.Command'] + self.oh.imports

        java_imports += '\n'.join('import {};'.format(i) for i in oh_imports) + '\n'

        return java_imports

    def get_java_class(self):
        java_class = super().get_java_class()
        java_class += '    public final static DeviceInfo DEVICE_INFO = new DeviceInfo(DEVICE_DISPLAY_NAME, "{}", DEVICE_IDENTIFIER, {}.class);\n\n'.format(self.get_name().lower_no_space, self.get_java_class_name())
        return java_class

    def get_filtered_elements_and_type(self, packet, elements, mapping):
        if mapping is not None:
            def f(e):
                val = mapping[e.get_name()]
                return val is not None and val.space != '__skip__'
            filtered_elements = [e for e in elements if f(e)]
        else:
            filtered_elements = elements

        if len(filtered_elements) > 1:
            type_ = packet.get_java_object_name(skip=-2 if packet.has_high_level() else 0)
        else:
            type_ = filtered_elements[0].get_java_type()

        return filtered_elements, type_

    def get_openhab_channel_init_code(self):
        init_code = []
        for c in self.oh.channels:
            if c.predicate != 'true':
                init_code += ['if ({}) {{'.format(c.predicate)]
                init_code += c.init_code.split('\n')
                init_code += ['}']
            else:
                init_code += c.init_code.split('\n')
        return init_code
    def get_openhab_callback_impl(self):
        lambda_transformation_template = """    private {type_} lambdaArgsTo{channel_camel}({callback_args}) {{
        {type_} lambda_transform_result{init};
        {assignments}
        return lambda_transform_result;
    }}"""

        # To init
        cb_registration = 'this.add{camel}Listener(({args}) -> {{if({filter}) {{{updateFn}.accept("{channel_camel}", transform{channel_camel}(lambdaArgsTo{channel_camel}({args})));}}}});'
        # To dispose
        cb_deregistration = 'this.listener{camel}.clear();'

        regs = []

        deregs = []
        dispose_code = []
        lambda_transforms = []
        for c in self.oh.channels:
            if c.callback_packet is None:
                continue
            name = common.FlavoredName(c.id).get()
            elements = c.callback_packet.get_elements(direction='out', high_level=True)
            regs.append(cb_registration.format(camel=c.callback_packet.get_name().camel,
                                               filter=c.callback_filter,
                                               channel_camel=common.FlavoredName(c.id).get().camel,
                                               args=', '.join(e.get_name().headless for e in elements),
                                               updateFn='triggerChannelFn' if c.is_trigger_channel else 'updateStateFn'))

            deregs.append(cb_deregistration.format(camel=c.callback_packet.get_name().camel))
            dispose_code += c.dispose_code.split('\n')

            filtered_elements, type_ = self.get_filtered_elements_and_type(c.getter_packet, elements, c.callback_param_mapping)

            if len(filtered_elements) > 1:
                init = ' = new {}()'.format(type_)
                if c.callback_param_mapping is None:
                    assignments = '\n\t\t'.join('lambda_transform_result.{0} = {0};'.format(e.get_name().headless) for e in filtered_elements)
                else:
                    assignments = []
                    for k, v in c.callback_param_mapping.items():
                        if v is None:
                            continue
                        assignments.append('lambda_transform_result.{} = {};'.format(k.headless, v.headless))
                    assignments = '\n\t\t'.join(assignments)
            else:
                init = ''
                if c.callback_param_mapping is None:
                    assignments = 'lambda_transform_result = {};'.format(filtered_elements[0].get_name().headless)
                else:
                    assignments = 'lambda_transform_result = {};'.format(c.callback_param_mapping[filtered_elements[0].get_name()].headless)

            lambda_transforms.append(lambda_transformation_template.format(type_=type_,
                                                                           channel_camel=name.camel,
                                                                           callback_args=', '.join(e.get_java_type() + ' ' + e.get_name().headless for e in elements),
                                                                           init=init,
                                                                           assignments=assignments))

        return (regs, deregs, dispose_code, lambda_transforms)

    def get_openhab_getter_impl(self):
        template = """    @Override
    public void refreshValue(String value, BiConsumer<String, State> updateStateFn, BiConsumer<String, String> triggerChannelFn) throws TinkerforgeException {{
        switch(value) {{
            {channel_cases}
        }}
        throw new RuntimeException("Refresh for unknown or trigger channel " + value + ". Should never happen.");
    }}
    """

        case_template = """case "{camel}":
               {updateFn}.accept(value, transform{camel}(this.{getter}({getter_params})));
               return;"""

        transformation_template = """    private {state_or_string} transform{camel}({type_} value) {{
        return {transform};
    }}"""

        channel_cases = []
        transforms = []
        for c in self.oh.channels:
            name = common.FlavoredName(c.id).get()
            channel_cases.append(case_template.format(camel=name.camel,
                                                      updateFn='triggerChannelFn' if c.is_trigger_channel else 'updateStateFn',
                                                      getter=c.getter_packet.get_name().headless,
                                                      getter_params=', '.join(c.getter_packet_params)))

            if c.callback_packet is not None:
                elements = c.callback_packet.get_elements(direction='out', high_level=True)
            else:
                elements = c.getter_packet.get_elements(direction='out', high_level=True)
            _, type_ = self.get_filtered_elements_and_type(c.getter_packet, elements, c.callback_param_mapping)

            transforms.append(transformation_template.format(state_or_string='String' if c.is_trigger_channel else 'State',
                                                             camel=name.camel,
                                                             type_=type_,
                                                             transform=c.transform))

        return (template.format(channel_cases='\n            '.join(channel_cases)), transforms)


    def get_openhab_setter_impl(self):
        template = """    @Override
    public void handleCommand(String channel, Command command) throws TinkerforgeException {{
        switch(channel) {{
            {channel_cases}
        }}
    }}"""

        case_template = """case "{camel}":
                if (command instanceof {command_type}) {{
                    {command_type} cmd = ({command_type}) command;
                    this.{setter}({setter_params});
                }}
                break;"""
        channel_cases = []
        for c in self.oh.channels:
            if c.setter_packet is None:
                continue
            name = common.FlavoredName(c.id).get()
            channel_cases.append(
                case_template.format(camel=name.camel,
                                     command_type=c.setter_command_type,
                                     setter=c.setter_packet.get_name().headless,
                                     setter_params=', '.join(c.setter_packet_params)))

        return template.format(channel_cases='\n            '.join(channel_cases))

    def get_openhab_channel_enablers(self):
        template = """if ({pred}) {{
                result.add("{channel_camel}");
            }}"""

        enablers = []
        for c in self.oh.channels:
            name = common.FlavoredName(c.id).get().camel
            if c.predicate == 'true':
                enablers.append('result.add("{channel_camel}");'.format(channel_camel=name))
            else:
                enablers.append(template.format(pred=c.predicate, channel_camel=name))

        return enablers

    def get_openhab_device_impl(self):
        template = """
    @Override
    public void initialize(Object config, BiConsumer<String, State> updateStateFn, BiConsumer<String, String> triggerChannelFn) throws TinkerforgeException {{
        {name_camel}Config cfg = ({name_camel}Config) config;
        {callback_registrations}
        {init_code}
    }}

    @Override
    public Class<{name_camel}Config> getConfigurationClass() {{
        return {name_camel}Config.class;
    }}

    @Override
    public void dispose(Object config) throws TinkerforgeException {{
        {callback_deregistrations}
        {dispose_code}
    }}

    @Override
    public List<String> getEnabledChannels(Object config) {{
        {name_camel}Config cfg = ({name_camel}Config) config;
        List<String> result = new ArrayList<String>();
        {channel_enablers}
        return result;
    }}

    {refresh_value}

    {handle_command}

    {transforms}
"""

        init_code = self.oh.init_code.split('\n') + self.get_openhab_channel_init_code()
        dispose_code = self.oh.dispose_code.split('\n')
        callback_regs, callback_deregs, callback_dispose_code, lambda_transforms = self.get_openhab_callback_impl()
        refresh_value, getter_transforms = self.get_openhab_getter_impl()
        handle_command = self.get_openhab_setter_impl()
        channel_enablers = self.get_openhab_channel_enablers()

        return template.format(name_camel=self.get_category().camel + self.get_name().camel,
                               init_code='\n\t\t'.join(init_code),
                               callback_registrations='\n\t\t'.join(callback_regs),
                               callback_deregistrations='\n\t\t'.join(callback_deregs),
                               dispose_code='\n\t\t'.join(callback_dispose_code + dispose_code),
                               channel_enablers='\n\t\t'.join(channel_enablers),
                               refresh_value=refresh_value,
                               handle_command=handle_command,
                               transforms='\n\t'.join(lambda_transforms + getter_transforms))

    def get_openhab_thing_xml(self):
        template = """<?xml version="1.0" encoding="UTF-8"?>
<thing:thing-descriptions bindingId="tinkerforge"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:thing="http://openhab.org/schemas/thing-description/v1.0.0"
    xsi:schemaLocation="http://openhab.org/schemas/thing-description/v1.0.0 http://openhab.org/schemas/thing-description-1.0.0.xsd">

    <thing-type id="{dev_name}">
        <label>Tinkerforge {name_space}</label>
        <description>{description}</description>

        <channels>
            {channels}
        </channels>
        <config-description>
{parameter_groups}
{parameters}
        </config-description>
    </thing-type>

{channel_types}
</thing:thing-descriptions>"""


        def get_channel_xml(c):
            template = """<channel id="{id}" typeId="{typeId}">
            {elems}
            </channel>"""
            elems = []
            if c.label is not None:
                elems.append('<label>{}</label>'.format(c.label))

            if c.description is not None:
                elems.append('<description>{}</description>'.format(c.description))

            return template.format(id=common.FlavoredName(c.id).get().camel,
                                   typeId=c.type_id,
                                   elems='\n'.join(elems))

        def get_parameter_group_xml(g):
            template = """            <parameter-group name="{name}">
                {elements}
            </parameter-group>"""
            return template.format(name=g.name, elements='\n                '.join('<{0}>{1}</{0}>'.format(k, v) for k, v in g.elements.items()))

        def get_parameter_xml(p):
            template = """            <parameter {attrs}>
                {elements}{options}{filter}
            </parameter>"""
            return template.format(attrs=' '.join('{}="{}"'.format(k, str(v)) for k, v in p.attrs.items()),
                                   elements='\n                '.join('<{0}>{1}</{0}>'.format(k, v) for k, v in p.elements.items()),
                                   options=common.wrap_non_empty('\n                <options>',
                                                                 '\n                    '.join('<option value="{}">{}</option>'.format(k, v) for k, v in p.options.items()),
                                                                 '\n                </options>'),
                                   filter=common.wrap_non_empty('\n                <filter>',
                                                                '\n                    '.join('<criteria name="{}">{}</criteria>'.format(k, v) for k, v in p.filter.items()),
                                                                '\n                </filter>'))


        def get_channel_type_xml(ct):
            template = """    <channel-type id="{type_id}">
		<item-type>{item_type}</item-type>
		<label>{label}</label>{description}{state}
	</channel-type>"""
            if all(x is None for x in [ct.min, ct.max, ct.pattern, ct.read_only]):
                state = ''
            else:
                state = '\n        <state {min}{max}{pattern}{readonly}/>'.format(
                    min='min="{}" '.format(ct.min) if ct.min is not None else '',
                    max='max="{}" '.format(ct.max) if ct.max is not None else '',
                    pattern='pattern="{}" '.format(ct.pattern) if ct.pattern is not None else '',
                    readonly='readOnly="{}" '.format(str(ct.read_only).lower()) if ct.read_only is not None else '')

            if ct.description is None:
                desc = ''
            else:
                desc = '\n        <description>{}</description>'.format(ct.description)

            return template.format(type_id=ct.type_id,
                                                item_type=ct.item_type,
                                                label=ct.label,
                                                description=desc,
                                                state=state)

        params = self.oh.params + [p for c in self.oh.channels for p in c.params]

        return template.format(dev_name=self.get_name().lower_no_space,
                               name_space=self.get_long_display_name(),
                               description=common.select_lang(self.get_description()),
                               channels='\n\t\t\t'.join(get_channel_xml(c) for c in self.oh.channels),
                               parameter_groups='\n\t\t\t'.join(get_parameter_group_xml(g) for g in self.oh.param_groups),
                               parameters='\n\t\t\t'.join(get_parameter_xml(p) for p in params),
                               channel_types='\n'.join(get_channel_type_xml(ct) for ct in self.oh.channel_types))

    def get_java_source(self, close_device_class=False):
        source =  super().get_java_source(close_device_class=False)
        source += self.get_openhab_device_impl()
        source += '}\n'
        return source

    def get_openhab_config_class(self):
        template = """package com.tinkerforge;{imports}

public class {name_camel}Config {{
    {parameters}

    public {name_camel}Config() {{}}
}}"""

        parameter_template = "{type} {name} = {ctor}{default}{ctor2};"

        params = self.oh.params + [p for c in self.oh.channels for p in c.params]

        param_types = {
            'integer': 'Integer',
            'decimal': 'BigDecimal',
            'boolean': 'Boolean',
            'text': 'String'
        }

        return template.format(imports='\n\nimport java.math.BigDecimal;' if 'decimal' in [p.type for p in params] else '',
                               name_camel=self.get_category().camel + self.get_name().camel,
                               parameters="\n\t".join(parameter_template.format(type=param_types[p.type],
                                                                                name=p.name.headless,
                                                                                ctor='new BigDecimal(' if p.type == 'decimal' else '',
                                                                                ctor2=')' if p.type == 'decimal' else '',
                                                                                default=p.default) for p in params))

    def get_openhab_binding_constant(self):
        template = """public static final ThingTypeUID {} = new ThingTypeUID(BINDING_ID, "{}");"""
        thing_type_caps = 'THING_TYPE_'+self.get_name().upper
        return (thing_type_caps, template.format(thing_type_caps, self.get_name().lower_no_space))


#     def get_java_listener_lists(self, template=''):
#         return super().get_java_listener_lists(template='\tprivate {0}Listener listener{0} = null;\n')

#     def get_java_callback_listener_definitions(self, listener_call_template=''):
#         return super().get_java_callback_listener_definitions(listener_call_template="""if (listener{name_camel} != null) {{
# {tab}	{listener_type} listener = listener{name_camel};
# {tab}	{listener_call}
# {tab}}}""")

#     def get_java_add_listener(self):
#         if self.get_callback_count() == 0:
#             return ''

#         template = """
# 	/**
# 	 * Sets the {0} listener.
# 	 */
# 	public void set{0}Listener({0}Listener listener) {{
# 		listener{0} = listener;
# 	}}

# 	/**
# 	 * Removes the {0} listener.
# 	 */
# 	public void remove{0}Listener() {{
# 		listener{0} = null;
# 	}}
# """
#         normal_low = [template.format(packet.get_name().camel) for packet in self.get_packets('callback')]
#         high = [template.format(packet.get_name(skip=-2).camel) for packet in self.get_packets('callback') if packet.has_high_level()]

#         return '\n'.join(normal_low + high)

class OpenHABBindingsGenerator(JavaBindingsGenerator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.released_devices = []

    def get_device_class(self):
        return OpenHABBindingsDevice

    def get_bindings_name(self):
        return 'openhab'

    def get_bindings_display_name(self):
        return 'OpenHAB'

    def is_openhab(self):
        return True

    def generate(self, device):
        if not 'openhab' in device.raw_data:
            return

        class_name = device.get_java_class_name()

        with open(os.path.join(self.get_bindings_dir(), class_name + '.java'), 'w') as f:
            f.write(device.get_java_source())

        with open(os.path.join(self.get_bindings_dir(), class_name + 'Config.java'), 'w') as f:
            f.write(device.get_openhab_config_class())

        with open(os.path.join(self.get_bindings_dir(), class_name + '.xml'), 'w') as f:
            f.write(device.get_openhab_thing_xml())

        if device.is_released():
            self.released_devices.append(device)
            self.released_files.append(class_name + '.java')
            self.released_files.append(class_name + 'Config.java')

    def finish(self):
        super().finish()
        consts = [d.get_openhab_binding_constant() for d in self.released_devices]
        thing_types = [x[0] for x in consts]
        uids = [x[1] for x in consts]

        common.specialize_template('TinkerforgeBindingConstants.java.template',
                                    os.path.join(self.get_bindings_dir(), 'TinkerforgeBindingConstants.java'),
                                    {
                                        '{uids}': '\n\t'.join(uids),
                                        '{thing_types}': ',\n\t\t'.join(thing_types)
                                    })
        common.specialize_template('DeviceFactory.java.template',
                                    os.path.join(self.get_bindings_dir(), 'DeviceFactory.java'),
                                    {
                                        '{devices}': ',\n\t\t\t'.join(d.get_java_class_name() + '.DEVICE_INFO' for d in self.released_devices)
                                    })

def generate(root_dir):
    common.generate(root_dir, 'en', OpenHABBindingsGenerator)

if __name__ == '__main__':
    generate(os.getcwd())
