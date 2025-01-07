# Line Py Webhook 環境快速安裝包

使用 Docker Compose 快速部署環境，這是一個以 Python 建置的 Webhook 伺服器，專為 LINE Messaging API 設計。當使用者傳送訊息給官方帳號時，Webhook 伺服器會自動回覆「您說了：+ 使用者傳的訊息」。由於此測試程式使用的是 Reply API，不會計入傳訊量費用，因此可以放心使用。

建議架設在雲端或 VPS 上，再搭配 Nginx 反向代理使用，請記得加入憑證，以確保該 Webhook 可以使用 HTTPS 連線，可以使用由 Let's Encrypt 提供免費的憑證服務。

### 首次安裝請依照以下步驟操作：

1. 請將此 Git 儲存庫 clone 到喜好的路徑下，接著 cd line_py_webhook
2. 執行 sh update_system.sh

### 資訊：

1. server port: 5000
