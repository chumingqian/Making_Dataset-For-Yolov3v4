import os
import json
import tqdm


def merge_json(path_results, path_merges):
    """
    主要功能是实现一个目录下的多个json文件合并为一个json文件。
    :param path_results:
    :param path_merges:
    :return:
    """
    merges_file = os.path.join(path_merges, "133.json")
    with open(merges_file, "w", encoding="utf-8") as f0:
        for file in os.listdir(path_results):
            with open(os.path.join(path_results, file), "r", encoding="utf-8") as f1:
                for line in tqdm.tqdm(f1):
                    line_dict = json.loads(line)
                    js = json.dumps(line_dict, ensure_ascii=False)
                    f0.write(js + '\n')
                f1.close()
        f0.close()


path_results, path_merges = "./epoch_results", "./"
if not os.path.exists(path_merges):  # 如果results目录不存在，新建该目录。
        os.mkdir(path_merges)
merge_json(path_results, path_merges)
