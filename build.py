# coding: utf-8
import yaml
import os
import json
from os import listdir
from os.path import isfile, isdir, join

def getMdTitle(path):
    with open(path, 'r') as file:
      line=file.readline()
      return line.replace("#","").strip()


def loadMain(path):
  data=None
  mainFile=f"{path}/main.yaml"
  if not os.path.isfile(mainFile):
    return None

  with open(mainFile, 'r') as file:
    data=yaml.load(file,Loader=yaml.FullLoader)

  #print(data)
  if data == None:
    return None

  mdFileList=[]
  allFilePaths=listdir(path)
  for f in allFilePaths:
    fullPath = join(path, f)
    if isfile(fullPath) and fullPath.endswith(".md"):
      mdFileList.append(f)
  data["mdFileInfos"] = []
  if data["mds"] == None:
    data["mds"]=[]

  for mdFile in mdFileList:
  #for mdFile in data["mds"]:
    if mdFile not in data["mds"]:
      data["mds"].append(mdFile)
    mdPath=f"{path}/{mdFile}"
    title=getMdTitle(mdPath)
    if title == "":
      title = mdFile.replace(".md", "").replace("_"," ")
    mdObj={"title": title, "name": mdFile, "path": mdPath.replace("./public/","")}
    data["mdFileInfos"].append(mdObj)



  data["path"]=path.replace("./public/", "")
  if data["nodes"] == None or len(data["nodes"]) ==0:
    return data

  subObjs=[]
  for i in range(len(data["nodes"])):
    node = data["nodes"][i]
    subPath=f"{path}/{node['name']}"
    subObj=loadMain(subPath)
    if subObj != None:
      subObjs.append(subObj)
      data["nodes"][i]["displayName"] = subObj["displayName"]
    else:
      data["nodes"][i]["displayName"] = node['name']

  data["nodeObjs"] = subObjs
  return data


mainData=loadMain("./public/md")

with open("./public/mdFiles.json", "w+", encoding='utf8') as mdF:
  json.dump(mainData, mdF, ensure_ascii=False)

print("build mdFiles end")
