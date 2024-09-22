import pandas

data_frame = pandas.read_csv('data/combined-small.csv.gz', compression='gzip')

print(data_frame)
print(data_frame['id'].head(20).to_list())
