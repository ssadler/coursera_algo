module Merge where

other :: [a] -> [a]
other [] = []
other (x:xs) = x : other (drop 1 xs)

merge :: Ord a => [a] -> [a] -> [a]
merge [] [] = []
merge [] xs = xs
merge xs [] = xs
merge (x:xs) (y:ys) = if (x < y)
                      then x : merge xs (y:ys)
                      else y : merge (x:xs) ys

mergesort :: Ord a => [a] -> [a]
mergesort [] = []
mergesort [x] = [x]
mergesort seq = merge (mergesort (other seq)) (mergesort (other (drop 1 seq)))

