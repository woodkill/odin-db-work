# CLAUDE.md

이 파일은 Claude Code(claude.ai/code)가 이 저장소의 코드로 작업할 때 지침을 제공합니다.

## 프로젝트들의 개요

- 이 일련의 프로젝트 모임을 **오딘카밀라** 프로젝트군이라고 명명합니다.
- **오딘카밀라** 프로젝트들은 '오딘 발할라라이징'이라는 MMORPG 게임 사용자들에게 편의를 제공하기 위한 목적으로 제작됩니다.
- `odin-botam-ocr` 프로젝트는 윈도우즈에서 실행되는 게임화면에서 보스 스폰 시간표를 파악하여 구글 Firebase firestore에 기록해 주는 앱을 제작하는 프로젝트입니다.
- `odin-camila`는 구글 'Compute Engine'에서 구동되는 Discord Bot을 제작하는 프로젝트입니다. 이 봇은 게임의 길드활동을 하기 위해 생성된 디스코드 서버에 초대되어 길드원들의 소통과 획득한 템의 분배, 보스를 잡을 때 출석한 길드원들의 출석체크 등 편의기능을 제공하며 특히 `odin-botam-ocr` 프로젝트에서 제작된 앱이 firestore에 업로드한 보스 출현시간 정보를 이용해 디스코드 음성채널에 알람 기능을 수행합니다.
- `odin-db-work`는 게임의 서버목록, 보스목록 등 게임의 마스터데이타성 자료들을 게임의 현재 상태에 맞게 관리하고 firestore에 업로드하기 위한 프로젝트입니다.
- `odin-common`은 오딘 카밀라 프로젝트들을 위한 공통 상수와 유틸리티를 포함한 Python 패키지입니다. 여러 오딘 관련 애플리케이션에서 표준화된 컬렉션(Collection), 문서(Document), 필드(Field)등 키값과 상수, 공유 기능을 제공하는 경량 공통 라이브러리입니다.

## 아키텍처

# odin-common 

프로젝트는 간단한 Python 패키지 구조를 따릅니다:
- **핵심 모듈**: `src/odin_common/`에 메인 패키지 코드가 포함됨
- **상수**: `constants.py`는 오딘 프로젝트 전반에서 사용되는 컬렉션 키들과 상수, 게임데이타들을 정의합니다.
- **주요패키지**:

이 프로젝트는 다음을 사용합니다:
- **빌드 시스템**: pyproject.toml 구성과 함께 setuptools 사용
- **Python 버전**: Python >=3.10 요구
- **패키지 구조**: 네임스페이스 패키지 구조를 가진 표준 src 레이아웃

# odin-db-work

- **핵심 모듈**: `main.py`에 기능별 주요 함수가 포함됨
- **사용방식**: 관리자가 필요에 따라 필요한 함수를 주석을 풀어서 실행시키는 방식
- **주요패키지**:

# odin-botam-ocr

- '작성해야 함'
- **주요패키지**:

# odin-camila

- '작성해야 함'
- **주요패키지**:

## 개발 명령어

### 설치 및 설정
```bash
# 개발 모드로 설치
pip install -e .

# requirements에서 설치 (나중에 추가될 경우)
pip install -r requirements.txt
```

### 빌드
```bash
# 패키지 빌드
python -m build
```

### 테스트
현재 테스트 프레임워크가 구성되지 않았습니다. 테스트를 추가할 때 적절한 테스트 명령어로 이 섹션을 업데이트하세요.

## 명명 규칙

### 상수 명명 규칙

Firestore 사용에 최적화된 명명 규칙을 사용합니다:

**1. Firestore 컬렉션**: `COL_` 접두사 사용
- Firestore 컬렉션명에 사용되는 상수
- 예: `COL_ODIN_DATA = "OdinData"`, `COL_GUILD_DATA = "OdinGuild2"`, `COL_BOSS_TIME = "BossTime"`
- 마이그레이션: `kCOL_ODINDATA` → `COL_ODIN_DATA`

**2. Firestore 문서**: `DOC_` 접두사 사용  
- Firestore 문서 ID나 문서명에 사용되는 상수
- 예: `DOC_USER_PROFILE = "UserProfile"`, `DOC_SERVER_CONFIG = "ServerConfig"`

**3. Firestore 필드명**: `K_` 접두사 사용
- Firestore 문서의 필드명에 사용되는 상수  
- Firestore 문서의 필드는 딕셔너리로 읽혀서 딕셔너리의 항목으로 사용되는 경우가 많으므로 같이 `K_` 접두사를 공통으로 사용
- 예: `K_LAST_UPDATED = "lastUpdated"`, `K_USER_ID = "userId"`

**4. 일반적인 키**: `K_` 접두사 사용
- 딕셔너리의 키값으로 사용되는 등 일반적인 문자열 키값에 사용  
- 예: `K_WIDTH = "width"`, `K_HEIGHT = "height"`

**5. 일반 값 상수**: `C_` 접두사 사용, 대문자_언더스코어 형식
- 상수를 의미하는 `C_` 접두사를 붙인다.
- 설정값, 기본값, 임계값 등 실제 값으로 사용되는 상수
- 예: `C_DEFAULT_TIMEOUT = 30`, `C_MAX_RETRY_COUNT = 3`, `C_API_BASE_URL = "https://api.example.com"`

**6. 상태(모드) 상수**: `S_`접두사를 맨 앞에 사용하고, 뒤에 오는 접두사로 그룹핑
- 맨 앞에 `S_` 접두사 사용
- 함께 관리되어야 하는 상태 관련된 상수들을 그룹핑하고 그것을 의미하는 두번째 접두사를 붙인다.
- 예: `S_USAGE_ACTIVE = "active"`, `S_USAGE_INACTIVE = "inactive"`

**7. 타입 상수**: `T_`접두사를 맨 앞에 사용하고, 뒤에 오는 접두사로 그룹핑
- 맨 앞에 `T_` 접두사 사용
- 함께 관리되어야 하는 타입들을 그룹핑하고 그것을 의미하는 두번째 접두사를 붙인다.
- 예: `T_BOSS_FIXED = 0`, `T_BOSS_INTERVAL = 1`, `T_BOSS_WEEKDAY_FIXED = 2`

## 리팩토링(Refactoring)

- `odin-common` 패키지를 사용하여 프로젝트들 간의 공통으로 사용되는 데이타의 일관성을 향상시키는 작업을 진행중입니다.
- 기존 `k` 접두사 코드에서 새로운 규칙으로 점진적으로 마이그레이션하세요.
- 기존 레거시 상수명을 사용하고 있는 것들은 모두 찾아서 새로운 규직으로 변경된 상수명으로 대체한다.