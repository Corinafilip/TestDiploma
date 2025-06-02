
   FROM python:3.12
   RUN apk update && apk upgrade  

   WORKDIR /usr/src/app
   RUN mkdir -p $WORKDIR
   ENV 

   RUN pip install --upgrade pip
   RUM cd $WORKDIR

   COPY ..
   RUN pip install -r requirements.txt

   EXPOSE 1212
   CMD ["python ", "manager.py", "runserver ". 1212"]





