import qualified Data.Char as C

digits :: Int -> [Int]
digits = map (\c -> C.ord c - C.ord '0') . show

step :: Int -> Int
step = sum . map (\x -> x*x) . digits

{- brute force -}
stepsReach89 :: Int -> Bool
stepsReach89 n
    | n == 89 = True
    | n == 1 = False
    | otherwise = stepsReach89 $ step n

{- memoized TODO -}
stepsReach89' :: Int -> Bool
stepsReach89' n = True

main = do
    putStrLn $ show $ sum $ map fromEnum $ map stepsReach89 $ [1..10000000]
