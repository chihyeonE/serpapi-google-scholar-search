# serpapi-google-scholar-search
Authorized Google Scholar Data Crawling with Serpapi

This Code has been tested on Conda Virtual Engine
이 코드는 Conda 환경에서만 테스트되었습니다.

# Initialize
환경 만들기


\'''bash
conda env create gs python
conda activate gs
conda install pip
conda install pandas
pip install serpapi
'''


구글 환경에서 검색 API를 공급받기 위해 SerpAPI 가입이 필요하다.

https://serpapi.com/dashboard

SerpAPI는 월 100회의 무료 검색을 지원한다.

로그인을 진행하고, Your Private API Key를 복사하여 sortgs_api.py의 다음 param dictionary 내부의 "api_key"에 넣어준다. (line 74)

\'''python
params = {
        "engine" : "google_scholar",
        "q" : keyword,
        "api_key" : "Your Private Key",
        "start" : n
    }
'''

# Usage

검색하고자 하는 키워드가
"Grating Coupler" "Lithium Niobate" "x-cut" "uniform" 이라고 해보자.

이 때, 이 키워드를 다음과 같이 변형시켜 인식할 수 있도록 한다. (띄어쓰기 -> + , " -> \")
\"grating+coupler\"+\"uniform\"+\"lithium+niobate\"+\"x-cut\"

뒤에 숫자는 검색하고자 하는 페이지 수로, n개 페이지에 대한 검색은 n*10개의 결과를 얻을 수 있다.

\'''bash 
  python sortgs_api.py \"grating+coupler\"+\"uniform\"+\"lithium+niobate\"+\"x-cut\" 12
'''

결과는 다음과 같이 Keyword.csv 형태로 제공되며 레포지토리에서 확인할 수 있다.
