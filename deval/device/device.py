# -*- coding: utf-8 -*-


class BaseDevice(object):
    
    def __init__(self):
        self.ComponentList = dict()
           
    def addComponent(self, com):
        self.ComponentList[com.com_name] = com

    def getComponent(self, name):
        return self.ComponentList.get(name)

    # Input Component Functions

    def click(self, *args, **kwargs):
        if "input" in self.ComponentList:
            return self.ComponentList["input"].click(*args, **kwargs)
        else:
            raise RuntimeError("No such component to perform click function")
    
    def tap(self, *args, **kwargs):
        return self.click(*args, **kwargs)

    def swipe(self, *args, **kwargs):
        if "input" in self.ComponentList:
            return self.ComponentList["input"].swipe(*args, **kwargs)
        else:
            raise RuntimeError("No such component to perform swipe function")

    def pinch(self, *args, **kwargs):
        if "input" in self.ComponentList:
            return self.ComponentList["input"].pinch(*args, **kwargs)
        else:
            raise RuntimeError("No such component to perform pinch function")

    def double_tap(self, *args, **kwargs):
        if "input" in self.ComponentList:
            return self.ComponentList["input"].double_tap(*args, **kwargs)
        else:
            raise RuntimeError("No such component to perform double_tap function")

    # Input Component Functions
    
    # KeyEvent Component Functions

    def keyevent(self, *args, **kwargs):
        if "keyevent" in self.ComponentList:
            return self.ComponentList["keyevent"].keyevent(*args, **kwargs)
        else:
            raise RuntimeError("No such component to perform keyevent function")

    def text(self, *args, **kwargs):
        if "keyevent" in self.ComponentList:
            return self.ComponentList["keyevent"].text(*args, **kwargs)
        else:
            raise RuntimeError("No such component to perform text function")

    def wake(self, *args, **kwargs):
        if "keyevent" in self.ComponentList:
            return self.ComponentList["keyevent"].wake(*args, **kwargs)
        else:
            raise RuntimeError("No such component to perform wake function")

    def home(self, *args, **kwargs):
        if "keyevent" in self.ComponentList:
            return self.ComponentList["keyevent"].home(*args, **kwargs)
        else:
            raise RuntimeError("No such component to perform home function")   

    # KeyEvent Component Functions        

    # Runtime Component Functions   

    def shell(self, *args, **kwargs):
        if "runtime" in self.ComponentList:
            return self.ComponentList["runtime"].shell(*args, **kwargs)
        else:
            raise RuntimeError("No such component to perform shell function")

    def kill(self, *args, **kwargs):
        if "runtime" in self.ComponentList:
            return self.ComponentList["runtime"].kill(*args, **kwargs)
        else:
            raise RuntimeError("No such component to perform kill function")

    # Runtime Component Functions   

    # App Component Functions   

    def start_app(self, *args, **kwargs):
        if "app" in self.ComponentList:
            return self.ComponentList["app"].start_app(*args, **kwargs)
        else:
            raise RuntimeError("No such component to perform start_app function")
        
    def stop_app(self, *args, **kwargs):
        if "app" in self.ComponentList:
            return self.ComponentList["app"].stop_app(*args, **kwargs)
        else:
            raise RuntimeError("No such component to perform stop_app function")

    def install(self, *args, **kwargs):
        if "app" in self.ComponentList:
            return self.ComponentList["app"].install(*args, **kwargs)
        else:
            raise RuntimeError("No such component to perform install function")

    def uninstall(self, *args, **kwargs):
        if "app" in self.ComponentList:
            return self.ComponentList["app"].uninstall(*args, **kwargs)
        else:
            raise RuntimeError("No such component to perform uninstall function")

    def start_app_timing(self, *args, **kwargs):
        if "app" in self.ComponentList:
            return self.ComponentList["app"].start_app_timing(*args, **kwargs)
        else:
            raise RuntimeError("No such component to perform start_app_timing function")
    
    def clear_app(self, *args, **kwargs):
        if "app" in self.ComponentList:
            return self.ComponentList["app"].clear_app(*args, **kwargs)
        else:
            raise RuntimeError("No such component to perform clear_app function")

    def install_app(self, *args, **kwargs):
        if "app" in self.ComponentList:
            return self.ComponentList["app"].install_app(*args, **kwargs)
        else:
            raise RuntimeError("No such component to perform install_app function")

    def install_multiple_app(self, *args, **kwargs):
        if "app" in self.ComponentList:
            return self.ComponentList["app"].install_multiple_app(*args, **kwargs)
        else:
            raise RuntimeError("No such component to perform install_multiple_app function")

    def uninstall_app(self, *args, **kwargs):
        if "app" in self.ComponentList:
            return self.ComponentList["app"].uninstall_app(*args, **kwargs)
        else:
            raise RuntimeError("No such component to perform uninstall_app function")
    
    def list_app(self, *args, **kwargs):
        if "app" in self.ComponentList:
            return self.ComponentList["app"].list_app(*args, **kwargs)
        else:
            raise RuntimeError("No such component to perform list_app function")

    def path_app(self, *args, **kwargs):
        if "app" in self.ComponentList:
            return self.ComponentList["app"].path_app(*args, **kwargs)
        else:
            raise RuntimeError("No such component to perform path_app function")

    def check_app(self, *args, **kwargs):
        if "app" in self.ComponentList:
            return self.ComponentList["app"].check_app(*args, **kwargs)
        else:
            raise RuntimeError("No such component to perform check_app function")

    # App Component Functions   
    
    # Screen Component Functions          

    def snapshot(self, *args, **kwargs):
        if "screen" in self.ComponentList:
            return self.ComponentList["screen"].snapshot(*args, **kwargs)
        else:
            raise RuntimeError("No such component to perform snapshot function")

    def move(self, *args, **kwargs):
        if "screen" in self.ComponentList:
            return self.ComponentList["screen"].move(*args, **kwargs)
        else:
            raise RuntimeError("No such component to perform move function")
    
    def get_current_resolution(self, *args, **kwargs):
        if "screen" in self.ComponentList:
            return self.ComponentList["screen"].get_current_resolution(*args, **kwargs)
        else:
            raise RuntimeError("No such component to perform get_current_resolution function")

    # Screen Component Functions

    # Getter Component 
    
    def get_ip_address(self, *args, **kwargs):
        if "getter" in self.ComponentList:
            return self.ComponentList["getter"].get_ip_address(*args, **kwargs)
        else:
            raise RuntimeError("No such component to perform getip function")

    def get_title(self, *args, **kwargs):
        if "getter" in self.ComponentList:
            return self.ComponentList["getter"].get_title(*args, **kwargs)
        else:
            raise RuntimeError("No such component to perform gettitle function")
    
    # Getter Component 


    


