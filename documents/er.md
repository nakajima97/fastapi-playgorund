```mermaid
erDiagram
  memos }|--|| users : ""
  users }|--|| companies : ""

  memos {
    bigint id PK
    bigint user_id
    string content "メモ本文"
  }

  users {
    bigint id PK
    bigint company_id
    string name "名前"
  }

  companies {
    bigint id PK
    string name "社名"
  }
```