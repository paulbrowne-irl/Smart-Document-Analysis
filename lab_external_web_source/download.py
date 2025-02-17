import nest_asyncio
from dpk_web2parquet.transform import Web2Parquet

''' Run an analysis of the files in directory marked path'''  
if __name__ == "__main__":
    # execute only if run as a script


    Web2Parquet(urls= ['http://directory.enterprise-ireland.com/'],
                    depth=2, 
                    downloads=100,
                    folder='downloads').transform()