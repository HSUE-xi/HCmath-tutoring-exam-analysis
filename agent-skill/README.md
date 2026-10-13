# 進階版：Codex / Claude Code

這是可安裝的 Agent Skill，**不是** Google Sheets 授權憑證。所有操作先預覽、確認，且只能修改本次新建分頁。

## 安裝（Windows PowerShell）

在這個 `agent-skill` 資料夾執行：

### Codex
```powershell
$dest = Join-Path $HOME '.agents\skills\tutoring-exam-analysis'
New-Item -ItemType Directory -Force $dest | Out-Null
Copy-Item .\SKILL.md -Destination $dest -Force
Copy-Item .\references, .\scripts -Destination $dest -Recurse -Force
```

### Claude Code
```powershell
$dest = Join-Path $HOME '.claude\skills\tutoring-exam-analysis'
New-Item -ItemType Directory -Force $dest | Out-Null
Copy-Item .\SKILL.md -Destination $dest -Force
Copy-Item .\references, .\scripts -Destination $dest -Recurse -Force
```

重新啟動工具，請它使用 `tutoring-exam-analysis`。每位同事必須另外配置 Google Sheets 寫入工具與相應權限；沒有工具只能產出人工操作計畫。避免把真實學生姓名、成績或金鑰提交到 GitHub。

## 試用
先使用 `test` 或新的測試分頁驗證，不覆蓋任何正式分頁。多選題扣分規則不明時停止並詢問。
