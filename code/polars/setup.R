# 0. Setup ----------------------------------------------------------------
{
  ## R libraries
  library(reticulate) 
  library(palmerpenguins)
  library(tidyverse)
  
  ## Set up python venv
  use_virtualenv("venv/")

  ## Load python libraries within R environment
  plt = import('matplotlib.pyplot')
  np = import('numpy')
  
  ## penguins scr
  dfa = palmerpenguins::penguins
  glimpse(dfa)
  
  }



# 1. Reproduce python output ----------------------------------------------
{
  
  # np.random.seed(19680801)  # https://github.com/rstudio/reticulate/issues/226
  np$random$seed(19680801L)
  
  # N = 50
  N <- 50L
  # x = np.random.rand(N)
  x <- np$random$rand(N)
  
  # y = np.random.rand(N)
  y <- np$random$rand(N)
  
  # colors = np.random.rand(N)
  colors <- np$random$rand(N)
  
  # area = (30 * np.random.rand(N))**2  # 0 to 15 point radii
  area <- (30 * np$random$rand(N))**2
  
  # plt.scatter(x, y, s=area, c=colors, alpha=0.5)
  plt$scatter(x, y, s=area, c=colors, alpha=0.5)
  
  # plt.show()
  plt$show()
}






