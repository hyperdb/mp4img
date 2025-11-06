import argparse
import os
import cv2


def main(inFile, outDir, seconds):
    # 入力ファイルの存在確認
    if not os.path.exists(inFile):
        print(f"エラー: 入力ファイル '{inFile}' が見つかりません。")
        return

    # 出力ディレクトリの作成
    os.makedirs(outDir, exist_ok=True)

    # 動画ファイルを開く
    cap = cv2.VideoCapture(inFile)
    if not cap.isOpened():
        print(f"エラー: 動画ファイル '{inFile}' を開けませんでした。")
        return

    # 動画の情報を取得
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps

    print(f"動画情報:")
    print(f"  FPS: {fps:.2f}")
    print(f"  総フレーム数: {total_frames}")
    print(f"  動画の長さ: {duration:.2f}秒")
    print(f"  {seconds}秒ごとにフレームを抽出します...")

    # フレーム抽出間隔（フレーム数）
    frame_interval = int(fps * seconds)

    frame_count = 0
    image_count = 1

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 指定間隔でフレームを保存
        if frame_count % frame_interval == 0:
            output_filename = os.path.join(outDir, f"{image_count:06d}.jpg")
            cv2.imwrite(output_filename, frame)
            current_time = frame_count / fps
            print(f"保存: {output_filename} (時刻: {current_time:.2f}秒)")
            image_count += 1

        frame_count += 1

    cap.release()
    print(f"処理完了: {image_count - 1}枚の画像を保存しました。")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="mp4ファイルから指定秒数ごとに静止画として保存します",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("inFile", help="処理対象のmp4ファイル")
    parser.add_argument("outDir", help="出力先のディレクトリ")
    parser.add_argument(
        "-s",
        "--seconds",
        type=int,
        default=10,
        help="何秒ごとに静止画を保存するかを指定します",
    )
    args = parser.parse_args()

    main(args.inFile, args.outDir, args.seconds)
