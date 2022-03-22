python3 train_ssd.py --dataset-type=voc --data=data/FTC-Objects-Model-Library --model-dir=models/FTC-Objects-Model-Library --batch-size=1 --workers=1 --epochs=1

python3 onnx_export.py --model-dir=models/FTC-Objects-Model-Library
