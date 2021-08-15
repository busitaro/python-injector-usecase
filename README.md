# python-injector-usecase
python injectorの簡単な使い方です。

## 各ファイルについて
|ファイル名|用途|
|----|----|
|main.py|DIの実行|
|interface.py|インターフェース、実装|
|di.py|インターフェースと実装の紐づけ|
<br>

注入するクラスを変更する際には、di.pyの以下の部分を変更して下さい。
```python
binder.bind(ISample, to=SampleLogic1)
```

## python injector
https://github.com/alecthomas/injector
