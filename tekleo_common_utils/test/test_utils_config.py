from tekleo_common_utils.utils_config import UtilsConfig

u = UtilsConfig()
p = 'config.ini'
u.load_config(p)
print(u.get_config_section_value(p, 'prod', 'url_1'))
print(u.get_config_section_value(p, 'local', 'url_1'))