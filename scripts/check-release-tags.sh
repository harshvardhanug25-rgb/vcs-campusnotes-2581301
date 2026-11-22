#!/usr/bin/env bash
set -euo pipefail

check_tag() {
  local tag=$1 expected_type=$2 ref="refs/tags/$1"
  local actual_type
  if ! actual_type=$(git cat-file -t "$ref" 2>/dev/null); then
    printf 'Missing tag %s. Fetch tags from the release repository first.\n' "$tag" >&2
    return 1
  fi
  if [[ "$actual_type" != "$expected_type" ]]; then
    printf '%s points to a %s object. Expected %s.\n' "$tag" "$actual_type" "$expected_type" >&2
    return 1
  fi
  git show -s --format="$tag ($actual_type) %h %s" "$ref^{commit}"
}

check_tag v0.1.0 commit
check_tag v1.0.0 tag
git merge-base --is-ancestor 'refs/tags/v0.1.0^{commit}' 'refs/tags/v1.0.0^{commit}'
