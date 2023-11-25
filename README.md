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


ИТОГОВЫЕ ВЕРСИИ МОДЕЛИ:
1) Предсказание Исполнителя: https://drive.google.com/file/d/1Ilvt-mq3C8fW8la2iMcuoCYu35Xu0Fjl/view
2) Предсказание Группы тем: https://drive.google.com/drive/folders/11DleA6bBUpUW3CRkVw4hKZJ-z6lR7-YS?usp=sharing
3) Предсказание Темы: https://drive.google.com/file/d/1fbMygBAYLOUgvybxF2LLfFTX2k-9MpAc/view?usp=sharing

