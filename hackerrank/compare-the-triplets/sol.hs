import Control.Monad
import Data.List

main :: IO ()
main = do
    ss <- forM [1,2] (\_ -> getLine)
    let [ns1, ns2] = map toInts ss
        (p1, p2) = foldl tupleSum (0,0) $ map scoresToPoints $ zip ns1 ns2
    putStrLn $ (show p1) ++" "++ (show p2)

toInts :: String -> [Int]
toInts = map read . words

scoresToPoints :: (Int,Int) -> (Int, Int)
scoresToPoints (n,m)
  | n > m = (1,0)
  | n == m = (0,0)
  | n < m = (0,1)

tupleSum :: (Int,Int) -> (Int,Int) -> (Int,Int)
tupleSum (n,m) (a,b) = (n+a,m+b)
