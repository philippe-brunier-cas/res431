cas_kable <- function(data, caption){
  tbl <- kable(data , caption = caption, align = 'c')
  return(tbl)
}

make_table_header <- function(header_path){
  header <- read_delim(header_path, delim=';', col_type=cols())
  
  header <- filter(header, grab>0)
  header <- header[-ncol(header)]
  
  cas_kable(header, caption='table')
  return(header)
}