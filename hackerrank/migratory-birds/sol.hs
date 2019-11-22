import Data.List
import Data.Function

sol :: [Int] -> Int
sol = head . head. sortBy (flip compare `on` length) . group . sort

main = interact $ show . sol . map read . tail . words
