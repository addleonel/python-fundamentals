
from bokeh.plotting import figure, show


if __name__ == '__main__':
    x_values = [2, 4, 6, 8, 3]
    y_values = []

    function = (lambda x: x**2)

    for x in x_values:
        x_values.append(function(x))

    p = figure(title='Square function', x_axis_label='x', y_axis_label='y')

    p.line(x_values, y_values, legend_label='square', line_width=2)

    show(p)
