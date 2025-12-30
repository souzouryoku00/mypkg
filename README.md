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

**基本的な実行（デフォルト設定）**

launchファイルを使用すると、送信側と受信側を同時に起動します。デフォルトでは「足し算 (+ 5)」を行います。

```
# 環境設定の読み込み、端末を新しく開いた際に初回のみ必須
source ~/ros2_ws/install/setup.bash
ros2 launch mypkg talk_listen.launch.py
```
実行結果:
```
[talker]: Publish: "0 + 5"
[listener]: Listen: "0 + 5" -> Answer: 5
```
終了するには Ctrl+C を入力してください。

**計算ルールの変更（パラメータ使用）**


