# Summary-Demo
簡易中文摘要系統API(使用TF-IDF)

### Documentation
#### Summary api
#### 🔗Route ```/summary/run```
#### ♟Action ```POST```
##### Request
```javascript
{
    "document"   : "按其在空氣中發生的部位，大概可分為雲中、雲間或雲地之間三大種類放電。雲中放電佔閃電的絕大多數，雲地之間放電者則是對人類的生產和生活產生影響的主要形式。",
    "topk": 3
}
```
##### Response
```javascript
{
    "data": {
        "summary": [
            {
                "score": 0.77504157320882,
                "sentence": "按其在空氣中發生的部位，大概可分為雲中、雲間或雲地之間三大種類放電。"
            },
            {
                "score": 0.77504157320882,
                "sentence": "雲中放電佔閃電的絕大多數，雲地之間放電者則是對人類的生產和生活產生影響的主要形式。"
            }
        ]
    },
    "message": "Summarize successfully."
}
```
## Installation
```bash
# Step 1 使用 git 下載專案
https://github.com/Amiannn/Summary-Demo.git
cd Summary-Demo

# Step 2 使用 Miniconda 建立虛擬 python 環境
conda create --name summer python=3.7
conda activate summer

# Step 3 安裝套件
pip3 install -r requirements.txt
```

## Run
```bash
python3 run.py
```

### Testing
- 可以使用 [Postman](https://www.postman.com/) 進行測試
