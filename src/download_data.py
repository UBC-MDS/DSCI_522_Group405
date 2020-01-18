import kaggle

kaggle.api.authenticate()

kaggle.api.dataset_download_files('dgomonov/new-york-city-airbnb-open-data', path='../data', unzip=True)
