import requests
from tqdm import tqdm


def download_dataset(url,dataset):
    with requests.get(url, stream = True) as r:
        r.raise_for_status()
        with open(dataset, 'wb') as j:
            pbar = tqdm(total=int(r.headers['Content-Length']))
            for chunk in r.iter_content(chunk_size = 8192):
                if chunk:
                    j.write(chunk)
                    pbar.update(len(chunk))
        
download_dataset("Dataset link paste here')    
