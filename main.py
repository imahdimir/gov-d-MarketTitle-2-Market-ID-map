##

"""

  """

##

from githubdata import GithubData
from mirutil.funcs import norm_fa_str as norm
from mirutil.funcs import save_df_as_a_nice_xl as sxl
from mirutil.funcs import read_data_according_to_type as rdata


map_repo_url = 'https://github.com/imahdimir/d-MarketTitle-2-MarketId'
cur_module_repo = 'https://github.com/imahdimir/gov-d-MarketTitle-2-MarketId'

mktitle = 'MarketTitle'
mktid = 'MarketId'

def main() :


  pass

  ##
  ufm = GithubData(map_repo_url)
  ufm.clone()
  ##
  fpn = ufm.data_filepath
  ##
  df = rdata(fpn)
  ##
  df = df[[mktitle, mktid]]
  ##
  df = df.applymap(norm)
  ##
  df = df.sort_values([mktid, mktitle])
  ##
  df = df.drop_duplicates()
  ##
  sxl(df , fpn)
  ##
  commit_msg = 'sorted'
  commit_msg += f' by repo: {cur_module_repo}'

  ufm.commit_push(commit_msg)
  ##
  ufm.rmdir()

  ##

##