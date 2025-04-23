function stem
    set fname (basename $argv[1])
    echo (string replace -r '\.[^.]+$' '' $fname)
end
