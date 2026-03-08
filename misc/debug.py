
y_prediction = 2.52
interval = .12

if y_prediction > 2.5:
    lower_bound = (y_prediction - interval).round(1) // 1
else:
    lower_bound = y_prediction - .5


higher_bound = (y_prediction + interval).round(1) // 1

lower_minutes = ((lower_bound % 1) * 60).round() 
higher_minutes = ((higher_bound % 1) * 60).round()

lower_bound_string = str(lower_bound.values).strip('[].')
higher_bound_string = str(higher_bound.values).strip('[].')
lower_minutes_string = str(lower_minutes.values).strip('[].')
higher_minutes_string = str(higher_minutes.values).strip('[].')
