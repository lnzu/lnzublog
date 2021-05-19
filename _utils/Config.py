import yaml,re

def getLZConfig():
    with open("config.yaml",encoding="utf-8") as f:
        try:
            m = yaml.load(f.read(),Loader=yaml.SafeLoader)
        except Exception as e:
            print(e)
        return m
        
def getThemePath():
    return "themes/"+getLZConfig()["themes"]+"/" 

def getThemeConfig():
    with open(getThemePath()+"_config.yaml",encoding="utf-8") as f:
        try:
            a = yaml.load(f.read(),Loader=yaml.SafeLoader)
        except Exception as e:
            print(e)
        return a
        
def getDomain():
    d = getLZConfig()['site']['domain']
    if d == '':
        return d
    else:
        return d+'/'
    
    
    
def getPostConfig(str):
    s = re.findall(r'\+{3,8}\n((.*\n){0,})\+{3,8}\n',str,re.M)
    return yaml.load(s[0][0],Loader=yaml.SafeLoader)
