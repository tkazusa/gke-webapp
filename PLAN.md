## Structure
root/
  - frontend/
    - Dockerfile
    - src/
      - frontend.py (かつてのapp.py)    
  
  - backend/
    - Dockerfile
    - src/
        - predict.py　(modelsから読み込んで推論するやつ)
        - backend.py (かつてのapp.pyの一部。推論結果をAPIにしてfrontendに返すやつ)
        - models/
          - rf.pkl  (一旦はローカルに置いてあるモデルをイメージにADDして、読み込むようにする。その後は、GitLFSとかから読み込んでADDでも良い気がする。)
        
  - configs/
    - backend-deployment.yaml
    - backend-service.yaml
    - frontend-deployment.yaml
    - frontend-service.yaml
          

```
frontendとbackendの間をRESTFUL AIPにする。
一旦はML忘れて、入力されたものを加工して返すだけでも良いかもしれない
```
