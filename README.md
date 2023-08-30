## Bank fraud detector
This web app was created as part of the *Antler Nordic Industry Sprint 1*.

It uses an **xgBoost** classifier trained by TÜRKAY AVCI that can be found on [kaggle](https://www.kaggle.com/code/turkayavci/fraud-detection-on-bank-payments). It was trained on a transformed [synthetic bank payments dataset](https://www.kaggle.com/datasets/ealaxi/banksim1).

In order to run it,
create a docker image by running
```console
docker build --tag frauddetector-app . 
```

and then running it by
```console
docker run --detach --publish 3100:3100 frauddetector-app
```

You can then open ```http://localhost:3100``` in your browser to access the API.



