# NeetCode practice (offline, Python)

All 150 NeetCode problems, across 18 topics. Nothing needs internet or any install beyond Python 3.

## Solve
Double-click `Start Practice.command`. The practice site opens in your browser. Keep the small window that appears open while you practice.

Pick a problem, write your code, and press **Run tests** (or Cmd+Enter). Your code saves as you type.

If macOS won't open the file, run this in a terminal from this folder instead:

    python3 server.py

You can also edit the files in `problems/` in VS Code. Reopen the problem on the site to see the change.

## On the site
- **Problem list:** search, filter by difficulty or status, and star problems to come back to.
- **My tests tab:** add your own cases. They run with Run tests but don't affect Solved. Stored in `my_tests/`.
- **Notes tab:** notes for each problem. Stored with stars in `progress.json`.
- **Layout:** drag the bars between panels to resize them. A− and A+ change the code size, and the button at the top right switches light and dark.
- **Timer:** press Timer at the top to start or pause it. It stops when all tests pass and clears when you change problem.
- **Reset code and Start over:** your code is copied to `backups/` first. After Reset code, Cmd+Z in the editor also brings it back. Your own tests, stars and notes stay.

## Commands (optional)
The site does all of this. These also work, run from this folder:

    python3 track.py                 show progress
    python3 track.py next            show the next unsolved problem
    python3 track.py test two_sum    run one problem's tests
    python3 track.py hint two_sum    show a hint
    python3 track.py answer two_sum  show a reference answer
    python3 track.py reset two_sum   blank one problem, with a backup
    python3 track.py reset all       blank everything, with a backup

## How progress works
All problems start blank. Solved status comes from your code: the tracker checks your files and runs their tests.
`[x]` means the tests pass, `[~]` means you've edited the file but it isn't passing, and `[ ]` means untouched.

Problem descriptions are original to this kit, not copied from LeetCode. The tests are small, so a pass is a good sign rather than proof.

## Credits
The problem list follows the NeetCode 150. Descriptions, tests, hints and answers here are original, and this project isn't affiliated with NeetCode or LeetCode. The code editor is [CodeMirror 5](https://codemirror.net/5/) (MIT license), in `web/vendor`.
