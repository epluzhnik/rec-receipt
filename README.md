1. Deploy

```sh
docker build -t rec-receipt. 
```
```sh
docker run -d --name rec-receipt -p 8000:8000 rec-receipt  
```

2. Swagger
> http://localhost:8000/docs

3. Run UI Demo
```sh
pip install -r front_requirements.txt
streamlit run front.py
``` 
