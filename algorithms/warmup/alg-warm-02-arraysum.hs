import Control.Applicative
import Control.Monad
import System.IO

main :: IO ()
main = do
  n_temp <- getLine
  let n = read n_temp :: Int
  ar_temp <- getLine
  let ar = map read $ words ar_temp :: [Int]
  putStrLn $ show $ foldl (+) 0 ar
