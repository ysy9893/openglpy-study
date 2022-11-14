import glfw 
import glad
import sys


class Window:
    def __init__(self, width:int, height:int, text:str):
        
        glfw.init()
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)#version
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)#version
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)#access to smaller subset of OpenGL features 
        self.windowG = glfw.create_window(width, height, "Learn OpenGL", None, None)
        if not self.windowG:
            sys.out("Failed to create GLFW window")
            glfw.terminate()
        glfw.make_context_current(self.windowG)
        glfw.set_framebuffer_size_callback(self.windowG, glfw._framebuffer_size_callback_repository)
        
    def loop(self):
        while(not glfw.window_should_close(self.windowG)):
            glfw.swap_buffers(self.windowG)
            glfw.poll_events()
        glfw.terminate()
    
        
if __name__ == "__main__":
    start_win = Window(1280, 720,"Opengl Window")
    start_win.loop()
    
        
        