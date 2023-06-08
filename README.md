# My Notebook (my-note)

This is my note

## 專案建構
- 執行npm run build
- 執行python3 `build.py`
- 只有加md檔或md檔的目錄，只需執行python3 `build.py`，然後上傳
- 要放md檔的子目錄，都需要建立main.yaml，格式請參照下方敘述


## main.yaml 格式:

1. name 填入當前路徑名
2. displayName 為在網頁上顯示的名稱
3. mds 為 md 檔案清單，可以不填，`build.py`會填入，但如果需要排序，則按所需順序排入，沒排入的會從後面排進
4. nodes 為該層的子目錄，用意除了列出子目錄外，也用於排序，陣列裡是放物件，物件中先只放目錄名稱 name，`build.py` 會額外填入 displayName
5. `build.py` 會填入 nodeoObjs，裡面會放子目錄的 main.yaml 轉成的物件
6. `build.py` 會填入 mdFileInfos，裡面為 md 檔檔名和 title(md 檔的第一行文字，去除#號)

```
name:
displayName:
mds:
  - test.md
nodes:
  - name:
```

## 需裝的python 套件
```
pip3 install pyyaml
```

## Install the dependencies

```bash
yarn
# or
npm install
```

### Start the app in development mode (hot-code reloading, error reporting, etc.)

```bash
quasar dev
```

### Lint the files

```bash
yarn lint
# or
npm run lint
```

### Format the files

```bash
yarn format
# or
npm run format
```

### Build the app for production

```bash
quasar build
```

### Customize the configuration

See [Configuring quasar.config.js](https://v2.quasar.dev/quasar-cli-vite/quasar-config-js).
