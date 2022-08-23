from app import df

from bokeh.plotting import figure,show,output_file

p=figure(x_axis_type='datetime', height=100, width=500, responsive=True, title='Motion Graph')
print(df)
p.yaxis.minor_tick_line_color = None
p.ygrid[0].ticker.desired_num_tick=1

q = p.quad(left='Start', right='End', bottom=0, top=1,color='green')

output_file('Graph1.html')
show(p)