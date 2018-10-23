import pyglet
import pyshaders
import math

frag = """
#version 130
out vec4 color_frag;
uniform vec3 color = vec3(1.0, 1.0, 1.0);
void main()
{
  color_frag = vec4(color, 1.0);
}
"""

vert = """
#version 130
in vec2 vert;
void main()
{
  gl_Position = vec4(vert, 1, 1);
}
"""


def triangle():
    return (-0.8, -0.8, 0.8, -0.8, 0, 0.8)


def start():
    window = pyglet.window.Window()
    shader = pyshaders.from_string(vert, frag)
    shader.use()

    tri = pyglet.graphics.vertex_list(3, ("v2f", triangle()))
    fps = pyglet.clock.ClockDisplay()

    t = 0

    def update(dt):
        nonlocal t
        t += dt
        shader.uniforms.color = (math.cos(t), math.sin(t), 0.5)

    pyglet.clock.schedule(update)

    @window.event()
    def on_draw():
        window.clear()
        tri.draw(pyglet.gl.GL_TRIANGLES)
        fps.draw()


if __name__ == "__main__":
    start()
    pyglet.app.run()
