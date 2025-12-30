# mypkg

ROS2を用いて数値と演算子を動的に設定し、計算式を送信・実行するノードです。

### 概要
* **Talker**: カウント変数とパラメータ（演算子・数値）を組み合わせて計算式（例: `"0 + 5"`）を生成し送信します。
* **Listener**: 受信した計算式を Python の `eval()` 関数で実行し、結果を出力します。

### 使い方

#### 1. リポジトリをクローン・ビルド

以下のコマンドでソースコードをクローン、ビルドしてください

```
cd ~/ros2_ws/src
git clone [https://github.com/souzouryoku00/mypkg.git](https://github.com/souzouryoku00/mypkg.git)
cd ~/ros2_ws
colcon build --symlink-install
```

#### 2. 実行方法

このパッケージは、Launchファイルで一括起動する方法と、個別の端末で別々に起動する方法のどちらでも動作します。※ どちらの方法でも、新しい端末を開たびに `source ~/ros2_ws/install/setup.bash` が必要です。
**方法1:Launchファイルを使用する**

送信側（Talker）と受信側（Listener）を1つのコマンドでまとめて起動します。

* **基本的な実行（デフォルト設定）**

launchファイルを使用すると、送信側と受信側を同時に起動します。デフォルトでは「足し算 (+ 5)」を行います。

```
source ~/ros2_ws/install/setup.bash
ros2 launch mypkg talk_listen.launch.py
```
実行結果:
```
[talker]: Publish: "0 + 5"
[listener]: Listen: "0 + 5" -> Answer: 5
[talker]: Publish: "1 + 5"
[listener]: Listen: "1 + 5" -> Answer: 6
```
終了するには Ctrl+C を入力してください。

* **計算ルールの変更（パラメータ使用）**

コマンドの引数で演算子 (symbol) や数値 (num) を指定できます。

掛け算の例 (* 10)
```
ros2 launch mypkg talk_listen.launch.py symbol:="'*'" num:=10
```
実行結果:
```
[talker]: Publish: "0 * 10"
[listener]: Listen: "0 * 10" -> Answer: 0
[talker]: Publish: "1 * 10"
[listener]: Listen: "1 * 10" -> Answer: 10
```

**方法2: 個別の端末で実行する**

ログを個別に確認したい場合や、デバッグを行いたい場合は、端末を2つ開いて実行します。

* **手順①: 受信側（Listener）の起動**
1つ目の端末で実行します。
```
source ~/ros2_ws/install/setup.bash
ros2 run mypkg listener
```
