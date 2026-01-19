# Exercise 4: Code Translation
Translate the following code snippets to Python using AI assistance:


## CODE 1: (Rust -> Python)

```rust
fn main() {
    let f = |x: f64| x.powi(2) - x;
    let a = 0.0;
    let b = 1.0;
    let n = 1000;
    let w = (b - a) / n as f64;
    let mut t = 0.0;
    for i in 0..n {
        let x = a + i as f64 * w;
        t += f(x) * w;
    }
    println!("The result is: {}", t);
}
```

## CODE 2: (Rust -> Python)

```rust
use std::collections::HashMap;

fn main() {
    let mut a: HashMap<&str, Vec<Vec<f64>>> = HashMap::new();

    a.insert("t1", vec![
        vec![1.0, 2.0, 3.0],
        vec![4.0, 5.0, 6.0],
        vec![7.0, 8.0, 9.0],
    ]);

    a.insert("t2", vec![
        vec![10.0, 11.0, 12.0],
        vec![13.0, 14.0, 15.0],
        vec![16.0, 17.0, 18.0],
    ]);

    a.insert("t3", vec![
        vec![19.0, 20.0, 21.0],
        vec![22.0, 23.0, 24.0],
        vec![25.0, 26.0, 27.0],
    ]);

    let mut b: HashMap<&str, HashMap<&str, f64>> = HashMap::new();

    for (&i, _) in &a {
        let mut tmp = HashMap::new();
        for (&j, _) in &a {
            let mut u = 0.0;
            for k in 0..a[i][0].len() {
                u += a[i][0][k] * a[j][1][k];
            }
            tmp.insert(j, u);
        }
        b.insert(i, tmp);
    }

    let mut c: HashMap<&str, HashMap<&str, f64>> = HashMap::new();

    for (&i, inner) in &b {
        let mut tmp = HashMap::new();

        let mut m = f64::NEG_INFINITY;
        for (_, &val) in inner {
            if val > m {
                m = val;
            }
        }

        let mut v = 0.0;
        for (_, &val) in inner {
            v += (val - m).exp();
        }

        for (&j, &val) in inner {
            tmp.insert(j, (val - m).exp() / v);
        }

        c.insert(i, tmp);
    }

    let mut d: HashMap<&str, Vec<f64>> = HashMap::new();

    for (&i, inner) in &c {
        let mut out = vec![0.0, 0.0, 0.0];

        for (&j, &w) in inner {
            for k in 0..a[j][2].len() {
                out[k] += w * a[j][2][k];
            }
        }

        d.insert(i, out);
    }

    println!("d =");
    for (k, v) in &d {
        println!("{} -> {:?}", k, v);
    }
}
```



## CODE 3 (Bash -> Python)


```bash
#!/bin/bash
# Ask for the folder name
echo "Enter the folder name: "
read folder_name
# Check if the folder exists
if [ ! -d "$folder_name" ]; then
echo "Folder does not exist."
exit 1
fi
# Get the list of files in the folder
files=( "$folder_name"/* )
# Rename each file by prepending "draft" to the file name
for file in "${files[@]}"; do
new_file_name="draft_$(basename "$file")"
mv "$file" "$new_file_name"
done
echo "Files renamed successfully."
```

