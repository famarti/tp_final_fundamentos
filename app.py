# leemos los arhivos de train, val y test
import pandas as pd
# df_train = pd.read_csv('train_timeseries.csv')
df_val = pd.read_csv('validation_timeseries.csv')
df_test = pd.read_csv('test_timeseries.csv')
# comparo validacion y test con sweetviz compare
import sweetviz as sv
report = sv.compare([df_val, "Validation"], [df_test, "Test"])
# guardo el reporte
report.show_html('compare.html', open_browser=False, layout='widescreen', scale=0.8, show_inline=True)