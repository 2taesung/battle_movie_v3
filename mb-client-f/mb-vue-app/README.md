# 오류들

## 0522

### 무비 리스트들을 for문으로 불러오기 실패



![스크린샷 2021-05-22 16.52.59](/Users/leetaesung/Desktop/git/movie_battle/mb-client-f/mb-vue-app/스크린샷 2021-05-22 16.52.59.png)



- 데이터 양이 너무 많아서 Vue는 깨지는 것으로 추측
- 처음에 페이지는 [] 으로 나왔다가 조금 시간이 지나니 갑자기 저래 변함
- 시간차가 있는거로 봐서는 ...
- 데이터는 vue에서 잘 넘어온다 조금 다르게 넣어보니d



https://kr.vuejs.org/v2/guide/list.html



### 해결

일단 인자를 넘길때 각각 키와 별개로 정의를 해줘야하고 v-for는 key 값 정의를 해줘야한다.  

```
    <BattleVote
      v-for="(movie, index) in movieList"
      :movie="movie"
      :key="movie.id"
    />
```

요래 해서 계속 헛스윙..



아래와 같이 해야한다.

```
    <BattleVote
      v-for="(movie, index) in movieList"
      :movie="movie"
      :index="index"
      :key="movie.id"
    />
```

내가 마스터로 작업을 했기 때문 나 역시 로컬에서 브랜치를 생성해 작업하면 된다.



## 0524

### git pull 했을때 vue가 안열리는 현상

![스크린샷 2021-05-25 12.29.34](/Users/leetaesung/Desktop/git/battle_movie_v3/mb-client-f/mb-vue-app/스크린샷 2021-05-25 12.29.34.png)

### 해결

https://stackoverflow.com/questions/51172064/command-not-found-with-vue-cli

npm을 지우고 다시 설치
