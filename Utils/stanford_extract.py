import json
from pathlib import Path
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

def extractGame(outputFolder, key, game):
    folderPath = f"{outputFolder}/{key}"
    filePath = f"{folderPath}/results_spotting.json"

    print(f"Creating folder {folderPath}...", end=" ")
    Path(folderPath).mkdir(parents=True, exist_ok=True)

    file = open(filePath, 'w')
    file.write(json.dumps(game, indent=4))
    file.close()
    print("Created!")

def loadFile(filePath):
    file = open(filePath)
    data = json.load(file)
    return data

def mergeGames(data):
    result = {}

    for game in data:
        gameName = game['video']
        half = gameName[-1]
        gameName = gameName[:-2]
        predictions = game['events']
        fps = game['fps']

        if (not(gameName in result)):
            result[gameName] = {
                "UrlLocal": gameName,
                "predictions": []
            }

        for pred in predictions:
            label = pred['label']
            frame = pred['frame']
            score = pred['score']
            millisecond = int(frame/fps*1000)
            minute = int(millisecond/1000/60)
            second = int(millisecond/1000)%60
            convertedPred = {
                'gameTime': '%s - %02d:%02d'%(half, minute, second),
                'label': label,
                "position": f'{millisecond}',
                "half": f"{half}",
                "confidence": f"{score}"
            }
            result[gameName]['predictions'].append(convertedPred)
    return result

def main(args):
    data = loadFile(args.path)
    merged = mergeGames(data)
    for key in merged:
        extractGame(args.output, key, merged[key])

if __name__=="__main__":
    
    parser = ArgumentParser(
        description="Construct stanford's output prediction to submit",
        formatter_class=ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "-p",
        "--path", 
        required=False,
        type=str,
        default="predictions.json",
        help="Path to prediction file"
    )

    parser.add_argument(
        "-o",
        "--output", 
        required=False,
        type=str,
        default="output",
        help="Output folder"
    )

    args = parser.parse_args()
    main(args)