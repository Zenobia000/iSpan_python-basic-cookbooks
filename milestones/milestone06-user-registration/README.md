# Milestone 6: 使用者註冊系統 | User Registration System

## 專案資訊 | Project Information

| 項目 | 內容 |
|:-----|:-----|
| **整合章節** | Ch20-Ch22 |
| **預計時數** | 8-10 小時 |
| **難度等級** | ⭐⭐⭐⭐ (高級) |
| **專案類型** | 安全認證系統 (Security Authentication System) |

---

## 專案目標 | Project Objectives

### 整合知識點
本專案整合以下章節的核心概念：

- **Ch20 例外處理 (Exception Handling)**: try/except/finally、例外階層、多重例外處理
- **Ch21 自訂例外 (Custom Exceptions)**: 自訂例外類別、raise 語句、例外鏈
- **Ch22 除錯技術 (Debugging Techniques)**: logging 模組、除錯策略、錯誤追蹤

### 學習目標
1. **例外處理設計**: 建立完整的例外處理機制
2. **自訂例外架構**: 設計層次化的例外類別系統
3. **安全驗證**: 實作密碼強度檢查與輸入驗證
4. **日誌系統**: 建立完整的操作記錄與錯誤追蹤
5. **系統穩定性**: 確保系統在各種錯誤情況下的穩定運行

---

## 專案描述 | Project Description

### 系統概述
設計一個**安全的使用者註冊與認證系統**，具備完整的例外處理機制、自訂例外類別、以及專業級的日誌記錄功能。系統須能處理各種錯誤情況並提供詳細的錯誤追蹤。

### 核心功能

#### 1. 使用者管理系統
- **註冊功能**: 新使用者註冊與資料驗證
- **登入功能**: 身份驗證與會話管理
- **登出功能**: 安全登出與會話清理
- **個人資料**: 查看與修改個人資訊
- **密碼管理**: 修改密碼與安全驗證

#### 2. 完整例外處理機制
```python
# 自訂例外階層架構
class UserSystemError(Exception):
    """使用者系統基礎例外"""
    pass

class ValidationError(UserSystemError):
    """資料驗證例外"""
    pass

class AuthenticationError(UserSystemError):
    """身份驗證例外"""
    pass

class SecurityError(UserSystemError):
    """安全性例外"""
    pass
```

#### 3. 安全驗證機制
- **使用者名稱驗證**: 長度、字元、唯一性檢查
- **密碼強度檢查**: 長度、複雜度、常見密碼檢查
- **電子郵件驗證**: 格式驗證與重複檢查
- **輸入清理**: 防止惡意輸入與 SQL 注入
- **登入嘗試限制**: 防暴力破解機制

#### 4. 專業日誌系統
```python
import logging

# 多層級日誌設定
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('user_system.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
```

#### 5. 操作介面
```
╔══════════════════════════════════════╗
║     使用者註冊系統 v2.0              ║
╚══════════════════════════════════════╝

【主選單】 - 未登入狀態
1. 使用者註冊
2. 使用者登入
3. 系統資訊
0. 結束程式

【會員選單】 - 已登入狀態
1. 查看個人資料
2. 修改個人資料
3. 修改密碼
4. 查看登入記錄
5. 登出
0. 結束程式

請選擇功能 (0-5):
```

---

## 學習成果 | Learning Outcomes

### 知識層面 (Knowledge)
- ✅ 理解例外處理的設計原則與最佳實踐
- ✅ 掌握自訂例外類別的層次架構設計
- ✅ 了解日誌系統的配置與應用
- ✅ 認識安全驗證的基本概念

### 技能層面 (Skills)
- ✅ 設計完整的例外處理機制
- ✅ 建立層次化的自訂例外類別
- ✅ 實作專業級的日誌記錄系統
- ✅ 處理複雜的錯誤情況與回復機制
- ✅ 實作安全的輸入驗證與資料處理

### 態度層面 (Attitude)
- ✅ 重視系統的穩定性與可靠性
- ✅ 培養防禦性程式設計思維
- ✅ 注重使用者體驗與錯誤訊息設計
- ✅ 建立安全意識與資料保護觀念

---

## 開發指南 | Development Guide

### 階段 1: 例外類別架構設計 (2 小時)

#### 步驟 1.1: 建立例外類別階層
```python
class UserSystemError(Exception):
    """使用者系統基礎例外類別

    所有系統相關例外的基礎類別，提供統一的錯誤處理介面。
    """
    def __init__(self, message, error_code=None, details=None):
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        self.details = details or {}
        self.timestamp = datetime.now()

    def __str__(self):
        return f"[{self.error_code}] {self.message}"

class ValidationError(UserSystemError):
    """資料驗證例外

    用於處理使用者輸入資料的驗證錯誤。
    """
    pass

class AuthenticationError(UserSystemError):
    """身份驗證例外

    用於處理登入、權限驗證相關錯誤。
    """
    pass

class SecurityError(UserSystemError):
    """安全性例外

    用於處理安全相關問題，如密碼強度、嘗試次數等。
    """
    pass

class DatabaseError(UserSystemError):
    """資料庫操作例外

    用於處理資料存取相關錯誤。
    """
    pass
```

#### 步驟 1.2: 建立日誌系統
```python
import logging
from datetime import datetime

class UserSystemLogger:
    """使用者系統日誌管理類別"""

    def __init__(self, name="UserSystem"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # 避免重複添加 handler
        if not self.logger.handlers:
            self._setup_handlers()

    def _setup_handlers(self):
        """設定日誌處理器"""
        # 檔案處理器 - 詳細日誌
        file_handler = logging.FileHandler(
            'user_system.log',
            encoding='utf-8'
        )
        file_handler.setLevel(logging.DEBUG)
        file_format = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'
        )
        file_handler.setFormatter(file_format)

        # 控制台處理器 - 簡化輸出
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_format = logging.Formatter(
            '%(levelname)s - %(message)s'
        )
        console_handler.setFormatter(console_format)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def info(self, message, **kwargs):
        """記錄資訊級別日誌"""
        self.logger.info(message, extra=kwargs)

    def warning(self, message, **kwargs):
        """記錄警告級別日誌"""
        self.logger.warning(message, extra=kwargs)

    def error(self, message, **kwargs):
        """記錄錯誤級別日誌"""
        self.logger.error(message, extra=kwargs)

    def debug(self, message, **kwargs):
        """記錄除錯級別日誌"""
        self.logger.debug(message, extra=kwargs)
```

**✅ 檢查點**:
- [ ] 例外類別階層架構完整
- [ ] 日誌系統能正常輸出到檔案與控制台
- [ ] 例外物件包含完整的錯誤資訊

---

### 階段 2: 資料驗證與安全機制 (3 小時)

#### 步驟 2.1: 輸入驗證模組
```python
import re
from typing import Dict, List

class InputValidator:
    """輸入驗證類別"""

    # 常見弱密碼列表
    COMMON_PASSWORDS = {
        "123456", "password", "123456789", "12345678", "12345",
        "1234567", "1234567890", "qwerty", "abc123", "Password"
    }

    @staticmethod
    def validate_username(username: str) -> None:
        """驗證使用者名稱

        Args:
            username: 使用者名稱

        Raises:
            ValidationError: 當使用者名稱不符合規則時
        """
        if not username:
            raise ValidationError(
                "使用者名稱不能為空",
                error_code="EMPTY_USERNAME"
            )

        if len(username) < 3:
            raise ValidationError(
                "使用者名稱至少需要 3 個字元",
                error_code="USERNAME_TOO_SHORT",
                details={"min_length": 3, "current_length": len(username)}
            )

        if len(username) > 20:
            raise ValidationError(
                "使用者名稱不能超過 20 個字元",
                error_code="USERNAME_TOO_LONG",
                details={"max_length": 20, "current_length": len(username)}
            )

        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            raise ValidationError(
                "使用者名稱只能包含英文字母、數字和底線",
                error_code="INVALID_USERNAME_CHARS"
            )

    @staticmethod
    def validate_password(password: str) -> None:
        """驗證密碼強度

        Args:
            password: 密碼

        Raises:
            SecurityError: 當密碼不符合安全要求時
        """
        if not password:
            raise SecurityError(
                "密碼不能為空",
                error_code="EMPTY_PASSWORD"
            )

        if len(password) < 8:
            raise SecurityError(
                "密碼至少需要 8 個字元",
                error_code="PASSWORD_TOO_SHORT",
                details={"min_length": 8, "current_length": len(password)}
            )

        if password.lower() in InputValidator.COMMON_PASSWORDS:
            raise SecurityError(
                "密碼過於簡單，請使用更安全的密碼",
                error_code="WEAK_PASSWORD"
            )

        # 檢查密碼複雜度
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)

        complexity_score = sum([has_upper, has_lower, has_digit, has_special])

        if complexity_score < 3:
            raise SecurityError(
                "密碼需要包含至少三種類型：大寫字母、小寫字母、數字、特殊符號",
                error_code="INSUFFICIENT_COMPLEXITY",
                details={
                    "has_upper": has_upper,
                    "has_lower": has_lower,
                    "has_digit": has_digit,
                    "has_special": has_special,
                    "score": complexity_score
                }
            )

    @staticmethod
    def validate_email(email: str) -> None:
        """驗證電子郵件格式

        Args:
            email: 電子郵件地址

        Raises:
            ValidationError: 當郵件格式無效時
        """
        if not email:
            raise ValidationError(
                "電子郵件不能為空",
                error_code="EMPTY_EMAIL"
            )

        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            raise ValidationError(
                "電子郵件格式無效",
                error_code="INVALID_EMAIL_FORMAT",
                details={"email": email}
            )
```

#### 步驟 2.2: 安全管理模組
```python
import hashlib
import secrets
from datetime import datetime, timedelta

class SecurityManager:
    """安全管理類別"""

    def __init__(self):
        self.failed_attempts = {}  # 記錄失敗嘗試
        self.max_attempts = 5      # 最大嘗試次數
        self.lockout_time = 300    # 鎖定時間 (秒)

    def hash_password(self, password: str) -> tuple:
        """加密密碼

        Args:
            password: 原始密碼

        Returns:
            tuple: (salt, hashed_password)
        """
        salt = secrets.token_hex(32)
        password_hash = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt.encode('utf-8'),
            100000
        )
        return salt, password_hash.hex()

    def verify_password(self, password: str, salt: str, stored_hash: str) -> bool:
        """驗證密碼

        Args:
            password: 輸入的密碼
            salt: 密碼鹽值
            stored_hash: 儲存的密碼雜湊

        Returns:
            bool: 密碼是否正確
        """
        password_hash = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt.encode('utf-8'),
            100000
        )
        return password_hash.hex() == stored_hash

    def check_login_attempts(self, username: str) -> None:
        """檢查登入嘗試次數

        Args:
            username: 使用者名稱

        Raises:
            SecurityError: 當嘗試次數過多時
        """
        if username in self.failed_attempts:
            attempt_info = self.failed_attempts[username]

            # 檢查是否仍在鎖定期間
            if attempt_info['locked_until'] > datetime.now():
                remaining_time = attempt_info['locked_until'] - datetime.now()
                raise SecurityError(
                    f"帳號已被鎖定，請在 {remaining_time.seconds} 秒後再試",
                    error_code="ACCOUNT_LOCKED",
                    details={
                        "locked_until": attempt_info['locked_until'],
                        "remaining_seconds": remaining_time.seconds
                    }
                )

            # 鎖定期已過，重置嘗試次數
            if attempt_info['locked_until'] <= datetime.now():
                self.failed_attempts[username] = {
                    'count': 0,
                    'locked_until': None
                }

    def record_failed_attempt(self, username: str) -> None:
        """記錄失敗嘗試

        Args:
            username: 使用者名稱
        """
        if username not in self.failed_attempts:
            self.failed_attempts[username] = {
                'count': 0,
                'locked_until': None
            }

        self.failed_attempts[username]['count'] += 1

        if self.failed_attempts[username]['count'] >= self.max_attempts:
            self.failed_attempts[username]['locked_until'] = (
                datetime.now() + timedelta(seconds=self.lockout_time)
            )

    def reset_failed_attempts(self, username: str) -> None:
        """重置失敗嘗試記錄

        Args:
            username: 使用者名稱
        """
        if username in self.failed_attempts:
            del self.failed_attempts[username]
```

**✅ 檢查點**:
- [ ] 輸入驗證能捕捉各種無效輸入
- [ ] 密碼強度檢查完整
- [ ] 登入嘗試限制機制運作正常
- [ ] 密碼加密與驗證功能正確

---

### 階段 3: 使用者管理系統 (3 小時)

#### 步驟 3.1: 使用者資料模型
```python
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

@dataclass
class User:
    """使用者資料模型"""
    username: str
    email: str
    password_hash: str
    salt: str
    created_at: datetime
    last_login: Optional[datetime] = None
    is_active: bool = True
    failed_login_count: int = 0
    profile: dict = None

    def __post_init__(self):
        if self.profile is None:
            self.profile = {}

@dataclass
class LoginSession:
    """登入會話模型"""
    username: str
    login_time: datetime
    session_id: str
    is_active: bool = True

class UserManager:
    """使用者管理類別"""

    def __init__(self):
        self.users = {}  # username -> User
        self.sessions = {}  # session_id -> LoginSession
        self.current_session = None
        self.logger = UserSystemLogger("UserManager")
        self.security = SecurityManager()

    def register_user(self, username: str, email: str, password: str,
                     profile: dict = None) -> None:
        """註冊新使用者

        Args:
            username: 使用者名稱
            email: 電子郵件
            password: 密碼
            profile: 個人資料

        Raises:
            ValidationError: 當輸入資料無效時
            DatabaseError: 當使用者已存在時
        """
        try:
            # 資料驗證
            InputValidator.validate_username(username)
            InputValidator.validate_email(email)
            InputValidator.validate_password(password)

            # 檢查使用者是否已存在
            if username in self.users:
                raise DatabaseError(
                    f"使用者名稱 '{username}' 已存在",
                    error_code="USERNAME_EXISTS",
                    details={"username": username}
                )

            # 檢查電子郵件是否已使用
            for user in self.users.values():
                if user.email == email:
                    raise DatabaseError(
                        f"電子郵件 '{email}' 已被使用",
                        error_code="EMAIL_EXISTS",
                        details={"email": email}
                    )

            # 加密密碼
            salt, password_hash = self.security.hash_password(password)

            # 建立使用者
            user = User(
                username=username,
                email=email,
                password_hash=password_hash,
                salt=salt,
                created_at=datetime.now(),
                profile=profile or {}
            )

            self.users[username] = user

            self.logger.info(
                f"使用者註冊成功: {username}",
                extra={"action": "register", "username": username}
            )

            print(f"✓ 使用者 '{username}' 註冊成功！")

        except (ValidationError, SecurityError, DatabaseError) as e:
            self.logger.error(
                f"使用者註冊失敗: {e}",
                extra={"action": "register", "error": str(e)}
            )
            raise
        except Exception as e:
            self.logger.error(
                f"註冊過程發生未預期錯誤: {e}",
                extra={"action": "register", "error": str(e)}
            )
            raise UserSystemError(
                "註冊過程發生錯誤，請稍後再試",
                error_code="REGISTRATION_FAILED"
            )

    def login_user(self, username: str, password: str) -> str:
        """使用者登入

        Args:
            username: 使用者名稱
            password: 密碼

        Returns:
            str: 會話ID

        Raises:
            AuthenticationError: 當認證失敗時
            SecurityError: 當帳號被鎖定時
        """
        try:
            # 檢查登入嘗試次數
            self.security.check_login_attempts(username)

            # 檢查使用者是否存在
            if username not in self.users:
                self.security.record_failed_attempt(username)
                raise AuthenticationError(
                    "使用者名稱或密碼錯誤",
                    error_code="INVALID_CREDENTIALS"
                )

            user = self.users[username]

            # 檢查帳號是否啟用
            if not user.is_active:
                raise AuthenticationError(
                    "帳號已被停用",
                    error_code="ACCOUNT_DISABLED"
                )

            # 驗證密碼
            if not self.security.verify_password(password, user.salt, user.password_hash):
                self.security.record_failed_attempt(username)
                user.failed_login_count += 1

                self.logger.warning(
                    f"登入失敗: {username} - 密碼錯誤",
                    extra={"action": "login_failed", "username": username}
                )

                raise AuthenticationError(
                    "使用者名稱或密碼錯誤",
                    error_code="INVALID_CREDENTIALS"
                )

            # 登入成功
            self.security.reset_failed_attempts(username)
            user.last_login = datetime.now()
            user.failed_login_count = 0

            # 建立會話
            session_id = secrets.token_urlsafe(32)
            session = LoginSession(
                username=username,
                login_time=datetime.now(),
                session_id=session_id
            )

            self.sessions[session_id] = session
            self.current_session = session

            self.logger.info(
                f"使用者登入成功: {username}",
                extra={"action": "login", "username": username, "session_id": session_id}
            )

            print(f"✓ 歡迎回來，{username}！")
            return session_id

        except (AuthenticationError, SecurityError) as e:
            self.logger.error(
                f"登入失敗: {e}",
                extra={"action": "login_failed", "error": str(e)}
            )
            raise
        except Exception as e:
            self.logger.error(
                f"登入過程發生未預期錯誤: {e}",
                extra={"action": "login_error", "error": str(e)}
            )
            raise UserSystemError(
                "登入過程發生錯誤，請稍後再試",
                error_code="LOGIN_FAILED"
            )
```

**✅ 檢查點**:
- [ ] 使用者註冊功能完整
- [ ] 登入驗證機制正確
- [ ] 會話管理功能運作
- [ ] 錯誤處理涵蓋所有情況

---

### 階段 4: 主程式與介面整合 (2 小時)

#### 步驟 4.1: 主程式架構
```python
class UserRegistrationSystem:
    """使用者註冊系統主程式"""

    def __init__(self):
        self.user_manager = UserManager()
        self.logger = UserSystemLogger("MainSystem")
        self.running = True

    def display_main_menu(self):
        """顯示主選單"""
        print("\n" + "="*50)
        print("  🔐 使用者註冊系統 v2.0")
        print("="*50)

        if self.user_manager.current_session:
            username = self.user_manager.current_session.username
            print(f"  目前登入：{username}")
            print("-"*50)
            print("1. 查看個人資料")
            print("2. 修改個人資料")
            print("3. 修改密碼")
            print("4. 查看登入記錄")
            print("5. 登出")
        else:
            print("  目前狀態：未登入")
            print("-"*50)
            print("1. 使用者註冊")
            print("2. 使用者登入")
            print("3. 系統資訊")

        print("0. 結束程式")
        print("="*50)

    def run(self):
        """主程式運行迴圈"""
        try:
            self.logger.info("系統啟動")
            print("🚀 使用者註冊系統啟動成功！")

            while self.running:
                try:
                    self.display_main_menu()
                    choice = input("請選擇功能 (0-5): ").strip()

                    if choice == "0":
                        self.shutdown()
                    elif self.user_manager.current_session:
                        self.handle_member_menu(choice)
                    else:
                        self.handle_guest_menu(choice)

                except KeyboardInterrupt:
                    print("\n\n⚠️  偵測到中斷信號，正在安全關閉系統...")
                    self.shutdown()
                except Exception as e:
                    self.logger.error(f"主程式發生錯誤: {e}")
                    print(f"❌ 系統錯誤: {e}")
                    print("請聯繫系統管理員或重新啟動程式")

        except Exception as e:
            self.logger.error(f"系統啟動失敗: {e}")
            print(f"❌ 系統啟動失敗: {e}")
        finally:
            self.cleanup()

    def shutdown(self):
        """安全關閉系統"""
        try:
            if self.user_manager.current_session:
                self.user_manager.logout_user()

            self.logger.info("系統正常關閉")
            print("👋 感謝使用，再見！")
            self.running = False

        except Exception as e:
            self.logger.error(f"關閉系統時發生錯誤: {e}")
            print(f"⚠️  關閉時發生錯誤: {e}")
            self.running = False

def main():
    """程式進入點"""
    system = UserRegistrationSystem()
    system.run()

if __name__ == "__main__":
    main()
```

**✅ 檢查點**:
- [ ] 主程式能正常啟動與關閉
- [ ] 選單系統運作流暢
- [ ] 錯誤處理機制完整
- [ ] 日誌記錄功能正常

---

## 評分標準 | Grading Rubric

### 例外處理機制 (30%)

| 項目 | 配分 | 評分標準 |
|:-----|:-----|:---------|
| 自訂例外類別 | 10% | - 建立完整的例外階層 (4%)<br>- 例外包含詳細資訊 (3%)<br>- 正確使用例外繼承 (3%) |
| try/except 使用 | 10% | - 適當的例外捕捉 (5%)<br>- 正確的例外處理邏輯 (5%) |
| 錯誤訊息設計 | 10% | - 訊息清晰易懂 (5%)<br>- 包含錯誤代碼 (5%) |

### 安全驗證機制 (25%)

| 項目 | 配分 | 評分標準 |
|:-----|:-----|:---------|
| 輸入驗證 | 10% | - 完整的資料驗證 (5%)<br>- 適當的驗證規則 (5%) |
| 密碼安全 | 10% | - 密碼強度檢查 (5%)<br>- 安全的密碼儲存 (5%) |
| 登入保護 | 5% | - 嘗試次數限制 (3%)<br>- 帳號鎖定機制 (2%) |

### 日誌系統 (20%)

| 項目 | 配分 | 評分標準 |
|:-----|:-----|:---------|
| 日誌配置 | 10% | - 多層級日誌設定 (5%)<br>- 格式化輸出 (5%) |
| 日誌內容 | 10% | - 完整的操作記錄 (5%)<br>- 錯誤追蹤資訊 (5%) |

### 系統功能 (15%)

| 項目 | 配分 | 評分標準 |
|:-----|:-----|:---------|
| 註冊功能 | 5% | 完整的使用者註冊流程 |
| 登入功能 | 5% | 安全的身份驗證機制 |
| 會話管理 | 5% | 登入狀態管理與登出 |

### 程式品質 (10%)

| 項目 | 配分 | 評分標準 |
|:-----|:-----|:---------|
| 程式架構 | 5% | - 模組化設計 (3%)<br>- 類別設計合理 (2%) |
| 註解文件 | 5% | - 完整的 docstring (3%)<br>- 適當的註解 (2%) |

---

## 教學建議 | Teaching Tips

### 評分重點

#### 1. 例外處理設計 (最重要)
- ✅ **優秀**: 建立完整的例外階層，每個例外類別有明確用途
- ⭐ **良好**: 使用基本的自訂例外，但階層不夠完整
- ❌ **不佳**: 只使用內建例外，沒有自訂例外類別

#### 2. 安全機制實作
- ✅ **優秀**: 完整的輸入驗證、密碼加密、登入保護
- ⭐ **良好**: 基本的驗證機制，但缺少部分安全功能
- ❌ **不佳**: 沒有適當的安全保護機制

#### 3. 日誌系統使用
- ✅ **優秀**: 專業級日誌配置，完整記錄系統操作
- ⭐ **良好**: 基本的日誌功能，但配置不夠完整
- ❌ **不佳**: 只使用 print 輸出，沒有正式日誌

### 常見問題與解決方案

#### 問題 1: 例外訊息不夠詳細
**解決方案**: 在例外中包含錯誤代碼和詳細資訊
```python
raise ValidationError(
    "使用者名稱長度不符",
    error_code="USERNAME_LENGTH",
    details={"min": 3, "max": 20, "current": len(username)}
)
```

#### 問題 2: 密碼以明文儲存
**解決方案**: 使用適當的雜湊演算法
```python
import hashlib
import secrets

salt = secrets.token_hex(32)
password_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)
```

#### 問題 3: 沒有適當的錯誤恢復機制
**解決方案**: 在 except 區塊中提供重試或替代方案
```python
try:
    # 主要邏輯
    pass
except SpecificError as e:
    logger.error(f"操作失敗: {e}")
    # 提供替代方案或重試機制
    return handle_alternative_flow()
```

### 教學時間分配建議

| 階段 | 時間 | 內容 |
|:-----|:-----|:-----|
| **理論講解** | 2 小時 | 例外處理原理、安全設計概念 |
| **示範開發** | 2 小時 | 例外類別設計、日誌系統建立 |
| **指導實作** | 3 小時 | 安全驗證機制、使用者管理系統 |
| **獨立開發** | 2 小時 | 完成剩餘功能與測試 |
| **程式檢討** | 1 小時 | 安全性檢查、最佳實踐分享 |

---

## 延伸挑戰 | Extension Challenges

### 挑戰 1: 進階安全機制 ⭐⭐⭐
實作更完整的安全功能：
- **雙因子認證 (2FA)**: 使用 TOTP 或 SMS 驗證
- **密碼歷史**: 防止重複使用舊密碼
- **會話過期**: 自動登出閒置使用者
- **IP 地址檢查**: 記錄並檢查異常登入位置

### 挑戰 2: 資料持久化 ⭐⭐⭐⭐
將資料儲存到資料庫：
```python
import sqlite3
import json

class DatabaseManager:
    def __init__(self, db_path="users.db"):
        self.db_path = db_path
        self.init_database()

    def init_database(self):
        """初始化資料庫結構"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    email TEXT UNIQUE,
                    password_hash TEXT,
                    salt TEXT,
                    created_at TEXT,
                    last_login TEXT,
                    profile TEXT
                )
            """)
```

### 挑戰 3: Web 介面整合 ⭐⭐⭐⭐⭐
使用 Flask 建立 Web 版本：
```python
from flask import Flask, request, session, render_template
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route('/register', methods=['GET', 'POST'])
def register():
    try:
        if request.method == 'POST':
            # 處理註冊邏輯
            pass
        return render_template('register.html')
    except ValidationError as e:
        return render_template('register.html', error=str(e))
```

### 挑戰 4: 進階日誌分析 ⭐⭐⭐
實作日誌分析功能：
- **使用者行為分析**: 統計登入時間、頻率
- **安全事件偵測**: 識別異常登入模式
- **效能監控**: 記錄系統回應時間
- **報表生成**: 自動產生安全報告

### 挑戰 5: 單元測試框架 ⭐⭐⭐⭐
建立完整的測試套件：
```python
import unittest
from unittest.mock import patch, MagicMock

class TestUserManager(unittest.TestCase):
    def setUp(self):
        self.user_manager = UserManager()

    def test_register_valid_user(self):
        """測試有效使用者註冊"""
        self.user_manager.register_user(
            "testuser", "test@email.com", "SecurePass123!"
        )
        self.assertIn("testuser", self.user_manager.users)

    def test_register_duplicate_username(self):
        """測試重複使用者名稱"""
        self.user_manager.register_user(
            "testuser", "test1@email.com", "SecurePass123!"
        )
        with self.assertRaises(DatabaseError):
            self.user_manager.register_user(
                "testuser", "test2@email.com", "SecurePass456!"
            )
```

---

## 相關資源 | Related Resources

### 複習章節
- **Ch20**: try/except/finally、例外階層、多重例外
- **Ch21**: 自訂例外類別、raise 語句、例外鏈
- **Ch22**: logging 模組、除錯策略、效能監控

### 延伸閱讀
- [Python 官方文件 - Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Python 官方文件 - Logging](https://docs.python.org/3/library/logging.html)
- [OWASP - Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/)
- [Real Python - Exception Handling](https://realpython.com/python-exceptions/)

### 安全資源
- [NIST - Digital Identity Guidelines](https://pages.nist.gov/800-63-3/)
- [OWASP - Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- [Python Security Best Practices](https://python-security.readthedocs.io/)

---

## 檢核清單 | Checklist

開發完成前，請確認以下項目：

### 功能檢核
- [ ] 使用者註冊功能正常運作
- [ ] 登入驗證機制完整
- [ ] 密碼強度檢查有效
- [ ] 登入嘗試限制功能正常
- [ ] 會話管理機制運作

### 例外處理檢核
- [ ] 建立完整的自訂例外階層
- [ ] 所有可能的錯誤都有適當處理
- [ ] 例外訊息清晰且有幫助
- [ ] 錯誤恢復機制完整

### 安全性檢核
- [ ] 密碼以加密方式儲存
- [ ] 輸入驗證涵蓋所有欄位
- [ ] 防暴力破解機制有效
- [ ] 沒有敏感資訊洩漏

### 日誌檢核
- [ ] 日誌系統配置正確
- [ ] 重要操作都有記錄
- [ ] 錯誤資訊完整記錄
- [ ] 日誌格式標準化

### 品質檢核
- [ ] 程式碼結構清晰
- [ ] 函式都有完整文件字串
- [ ] 關鍵邏輯有註解說明
- [ ] 符合 Python 編碼規範

---

**建立安全可靠的系統，保護使用者資料！**