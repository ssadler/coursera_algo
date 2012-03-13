import System.Random
import System.Environment
import Data.List
import Merge

main = do
    argv <- getArgs
    seed  <- newStdGen
    print $ head $ mergesort $ randomlist (read (head argv)) seed


randomlist :: Int -> StdGen -> [Int]
randomlist n = take n . unfoldr (Just . random)
