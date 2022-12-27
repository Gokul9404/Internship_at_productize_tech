import cv2
import os
# =============================================
videoStartTimeInSeconds = 0
videoEndTimeInSeconds = 360
# inputVideoPath="E:\\Internship\\12-dec-vedio\\vedios"
Video_folder = "E:\\Internship\\New folder\\az"
# =============================================
def main():
        x = 2311
        for count, _ in enumerate(os.listdir(Video_folder)):
                dst = f"ved_{str(count+16)}"
                inputVideoPath = f"{Video_folder}\\{dst}.mov"
                print(inputVideoPath)
                video = cv2.VideoCapture(inputVideoPath)
                fpsOfVideo = int(video.get(cv2.CAP_PROP_FPS))
                stepSize = int(fpsOfVideo/2)
                print(fpsOfVideo)
                # print(stepSize)
                startFrame = videoStartTimeInSeconds * fpsOfVideo
                endFrame = videoEndTimeInSeconds * fpsOfVideo

                os.mkdir(f"{Video_folder}\\{dst} frame")
                # =============================================
                for currentFrameNumber in range(startFrame, endFrame,stepSize):
                        try:
                                video.set(cv2.CAP_PROP_POS_FRAMES, currentFrameNumber)
                                _, frame = video.read()
                                cv2.imwrite(f"{Video_folder}\{dst} frame\\Img_{x}.jpg", frame)
                                x += 1
                        except Exception as e:
                                # print(e)
                                break
                # print(count)
                # print(counter)

if __name__ == '__main__':
    main()