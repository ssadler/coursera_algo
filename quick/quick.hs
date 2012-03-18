import Data.List

pivot :: Ord a => a -> [a] -> [a] -> [a] -> [a]
pivot n [] xs ys = quicksort xs ++ quicksort ys
pivot n (x:xs) ys zs = if (x < n)
                       then pivot n xs (x:ys) zs
                       else pivot n xs ys (x:zs)


quicksort :: Ord a => [a] -> [a]
quicksort [] = []
quicksort [x] = [x]
quicksort xs = pivot (xs !! round (realToFrac (length xs) / 2)) xs [] []
